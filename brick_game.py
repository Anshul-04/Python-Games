import pygame


# Initialize Pygame
pygame.init()

# Set screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Pygame Test")

# Fill the screen with white
screen.fill((255, 255, 255))

# Update the display
pygame.display.flip()

# Main loop
running = True
while running:
    # Check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

# Print success message
print("Pygame seems to be working!")
