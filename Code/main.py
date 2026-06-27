import time
import subprocess
import sys
import platform
import os

# ==========================================
# 0. AUTO-INSTALLER & HARDWARE SETUP
# ==========================================
def setup_pi_hardware():
    """Checks and configures the Raspberry Pi's config.txt for Software I2C"""
    # Newer Raspberry Pi OS (Bookworm) uses /boot/firmware. Older uses /boot.
    config_paths = ["/boot/firmware/config.txt", "/boot/config.txt"]
    config_file = None
    
    for path in config_paths:
        if os.path.exists(path):
            config_file = path
            break
            
    if not config_file:
        print("[-] Could not find config.txt! Are you sure this is a Raspberry Pi?")
        return

    target_line = "dtoverlay=i2c-gpio,i2c_gpio_sda=27,i2c_gpio_scl=22"
    
    # Check if the line is already in the file
    with open(config_file, "r") as f:
        content = f.read()
        
    if target_line not in content:
        print(f"\n[!] First-time setup: Enabling Software I2C on GPIO 27 & 22...")
        # We have to use a terminal command to append the line because it requires 'sudo'
        append_cmd = f"echo '\n# Enabled by Everest Minishot\n{target_line}' | sudo tee -a {config_file}"
        subprocess.run(append_cmd, shell=True)
        
        print("\n[+] Hardware config updated! The Raspberry Pi MUST reboot to apply this.")
        print("[!] Rebooting in 5 seconds... Please run the script again after boot!")
        time.sleep(5)
        subprocess.run(["sudo", "reboot"])
        sys.exit(0)

def run_auto_installer():
    current_os = platform.system()
    print("\n[!] Missing dependencies detected. Starting Auto-Installer...\n")
    if current_os == "Linux":
        print("-> Raspberry Pi detected. Running APT installer...")
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", "python3-gpiozero", "python3-tk", "python3-pil", "python3-pil.imagetk", "python3-opencv", "python3-luma-oled"])
        print("\n[+] Install complete! Running hardware check...")
        setup_pi_hardware() # Run the hardware setup right after installing!
        
        print("\n[+] All setup complete! Please run the script one more time.")
        sys.exit(0)
    elif current_os == "Darwin":
        print("-> Mac detected. You are missing dependencies.")
        print("-> Run this in terminal: pip3 install opencv-python Pillow")
        sys.exit(1)

# Check hardware config immediately if we are on a Pi
if platform.system() == "Linux":
    setup_pi_hardware()

# ==========================================
# 1. ENVIRONMENT & LIBRARY DETECTION
# ==========================================
# (The rest of your code continues exactly as before...)