import time
import subprocess
import sys
import platform
import os

# ==========================================
# 0. AUTO-INSTALLER BOOTSTRAPPER 
# ==========================================
def run_auto_installer():
    current_os = platform.system()
    print("\n[!] Missing dependencies detected. Starting Auto-Installer...\n")
    if current_os == "Linux":
        print("-> Raspberry Pi detected. Running APT installer...")
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", "python3-gpiozero", "python3-tk", "python3-pil", "python3-pil.imagetk", "python3-opencv"])
        print("\n[+] Install complete! Please run the script one more time.")
        sys.exit(0)
    elif current_os == "Darwin":
        print("-> Mac detected. You are missing dependencies.")
        print("-> Run this in terminal: pip3 install opencv-python Pillow")
        sys.exit(1)

# ==========================================
# 1. ENVIRONMENT & LIBRARY DETECTION
# ==========================================
try:
    import tkinter as tk
    from PIL import Image, ImageTk
except ImportError:
    run_auto_installer()

try:
    from gpiozero import Button
    IS_PI = True
    print("[+] Raspberry Pi detected! Hardware controls active.")
except ImportError:
    IS_PI = False
    print("[+] Mac detected! Simulator mode active.")

try:
    import cv2
    HAS_CV2 = True
    print("[+] OpenCV detected! Live viewfinder is active.")
except ImportError:
    HAS_CV2 = False
    if not IS_PI:
        print("[-] OpenCV missing! Please run: pip3 install opencv-python")

# Global variables
current_mode = "PHOTO"
photo_count = 0
cap = None 
current_frame = None 

# ==========================================
# 2. CORE CAMERA LOGIC
# ==========================================
def capture_media(event=None):
    global photo_count, current_frame
    photo_count += 1
    
    status_label.config(text="Capturing...", fg="red")
    root.update()
    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"img_{timestamp}.jpg"
    
    if current_mode == "PHOTO":
        if IS_PI and not HAS_CV2:
            print(f"📸 Click! Saving photo: {filename}")
            # subprocess.run(["libcamera-still", "-o", f"/home/pi/Pictures/{filename}"])
            time.sleep(0.5)
        else:
            if HAS_CV2 and current_frame is not None:
                save_frame = cv2.cvtColor(current_frame, cv2.COLOR_RGB2BGR)
                cv2.imwrite(filename, save_frame)
                print(f"📸 SNAP! Saved live frame to: {filename}")
            else:
                print(f"📸 Click! (Simulated) Saving photo: {filename}")
                time.sleep(0.5)
            
    elif current_mode == "VIDEO":
        print(f"🎥 Recording 5 seconds... Saving video: vid_{timestamp}")
        time.sleep(5)

    status_label.config(text="Ready", fg="white")
    count_label.config(text=f"Files: {photo_count}")
    root.update()

def toggle_mode(event=None):
    global current_mode
    if current_mode == "PHOTO":
        current_mode = "VIDEO"
        mode_label.config(text="📹 VIDEO", fg="#3498db")
    else:
        current_mode = "PHOTO"
        mode_label.config(text="📸 PHOTO", fg="#f1c40f")
    print(f"Switched to {current_mode} mode.")

def safe_shutdown(event=None):
    status_label.config(text="SHUTTING DOWN...", fg="red")
    root.update()
    time.sleep(1.5)
    
    if HAS_CV2 and cap is not None:
        cap.release() 
        
    if IS_PI:
        print("Powering down Raspberry Pi... Goodnight!")
        subprocess.run(["sudo", "shutdown", "-h", "now"])
    else:
        print("Closing simulator... Goodnight!")
        root.destroy() 

# ==========================================
# 3. DYNAMIC LIVE VIEWFINDER
# ==========================================
def update_viewfinder():
    global current_frame
    if HAS_CV2 and cap is not None:
        ret, frame = cap.read()
        if ret:
            # 1. Get the current size of the Tkinter window
            # We subtract ~100px from the height to leave room for the top and bottom text bars
            target_width = root.winfo_width()
            target_height = root.winfo_height() - 100 
            
            # Failsafe: Tkinter sometimes reports 1x1 pixels before the window fully opens
            if target_width < 10:
                target_width = 320
                target_height = 140

            # 2. Get the actual native resolution of the webcam
            h, w, _ = frame.shape
            
            # 3. Calculate the perfect scaling math so it doesn't stretch weirdly
            scale = min(target_width / w, target_height / h)
            new_w = int(w * scale)
            new_h = int(h * scale)
            
            # 4. Resize and convert for Tkinter
            frame = cv2.resize(frame, (new_w, new_h))
            current_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(current_frame)
            imgtk = ImageTk.PhotoImage(image=img)
            
            viewfinder_label.imgtk = imgtk
            viewfinder_label.configure(image=imgtk)
            
    root.after(30, update_viewfinder)

# ==========================================
# 4. USER INTERFACE (Tkinter)
# ==========================================
root = tk.Tk()
root.title("Everest Minishot")
root.configure(bg="black")

# Make it massive on Mac, but perfectly fullscreen on the tiny Pi!
if IS_PI:
    root.geometry("320x240")
    root.attributes("-fullscreen", True)
else:
    root.geometry("800x600")

# Top Bar (Mode)
mode_label = tk.Label(root, text="📸 PHOTO", font=("Helvetica", 14, "bold"), bg="black", fg="#f1c40f")
mode_label.pack(side="top", pady=5)

# Center Screen (Live Viewfinder)
viewfinder_label = tk.Label(root, bg="gray10", text="Camera Off", fg="white")
viewfinder_label.pack(expand=True)

# Bottom Bar (Status & Count)
bottom_frame = tk.Frame(root, bg="black")
bottom_frame.pack(side="bottom", fill="x", padx=10, pady=5)

count_label = tk.Label(bottom_frame, text="Files: 0", font=("Helvetica", 10), bg="black", fg="gray")
count_label.pack(side="left")

status_label = tk.Label(bottom_frame, text="Ready", font=("Helvetica", 10), bg="black", fg="white")
status_label.pack(side="right")

# ==========================================
# 5. HARDWARE INIT & INPUT ROUTING
# ==========================================
if HAS_CV2:
    cap = cv2.VideoCapture(0)
    update_viewfinder() 

if IS_PI:
    mode_button = Button(3, hold_time=3) 
    shutter_button = Button(4, pull_up=True, bounce_time=0.1)

    shutter_button.when_pressed = capture_media
    mode_button.when_pressed = toggle_mode
    mode_button.when_held = safe_shutdown
else:
    root.bind("<space>", capture_media)
    root.bind("m", toggle_mode)
    root.bind("q", safe_shutdown)

root.mainloop()