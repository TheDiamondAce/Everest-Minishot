import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Define screen dimensions for your OLED (e.g., 128x64 pixels)
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Camera UI')

# Define Colors (OLEDs are typically monochrome: Black and White)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load a tiny, pixel-clear font for the small screen
font = pygame.font.SysFont('Arial', 12)

# Camera States
modes = ["PHOTO", "VIDEO", "GALLERY", "SETTINGS"]
current_mode_index = 0
battery_level = 85  # Mock percentage from power management
photos_left = 420   # Mock space left on SD card

# Main Game Loop Flag
running = True
clock = pygame.time.Clock()

while running:
    # 1. HANDLE INPUTS (Mocking your GPIO pins with Keyboard for testing on your PC)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            # Mocking the Rotary Encoder Turn (Left/Right Arrows)
            if event.key == pygame.K_RIGHT:
                current_mode_index = (current_mode_index + 1) % len(modes)
                print(f"Mode changed to: {modes[current_mode_index]}")
            elif event.key == pygame.K_LEFT:
                current_mode_index = (current_mode_index - 1) % len(modes)
                print(f"Mode changed to: {modes[current_mode_index]}")
                
            # Mocking Shutter Button Half-Press (F key for Focus)
            elif event.key == pygame.K_f:
                print("Autofocus Triggered...")
                
            # Mocking Shutter Button Full-Press (Spacebar to Shoot)
            elif event.key == pygame.K_SPACE:
                print("SNAP! Photo Taken.")

    # 2. DRAW THE INTERFACE
    screen.fill(BLACK) # Clear screen with black baseline

    # Draw Top Status Bar (Battery and Storage)
    battery_text = font.render(f"BAT: {battery_level}%", True, WHITE)
    storage_text = font.render(f"REM: {photos_left}", True, WHITE)
    screen.blit(battery_text, (5, 2))
    screen.blit(storage_text, (75, 2))
    pygame.draw.line(screen, WHITE, (0, 16), (SCREEN_WIDTH, 16), 1) # Divider line

    # Draw Center Mode Selector
    current_mode_text = font.render(modes[current_mode_index], True, WHITE)
    # Center the text horizontally
    text_rect = current_mode_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 5))
    screen.blit(current_mode_text, text_rect)

    # Draw UI Decorative Corners (Makes it look like a camera viewfinder)
    pygame.draw.rect(screen, WHITE, (2, 20, 5, 2))  # Top Left
    pygame.draw.rect(screen, WHITE, (2, 20, 2, 5))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 7, 20, 5, 2)) # Top Right
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 4, 20, 2, 5))

    # 3. UPDATE THE DISPLAY
    pygame.display.flip()
    
    # Cap the frame rate at 30 FPS to prevent the Pi Zero from overheating
    clock.tick(30)

pygame.quit()
sys.exit()