import pygame
import sys

# Initialize Pygame
pygame.init()

# Initialize display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

# Initialize player
player = {
    "x": 0,
    "y": 0,
    "width": 64,
    "height": 64,
    "speed": 10,
}

# Initialize clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Properly shutdown when user closes window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Respond to currently pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player["x"] -= player["speed"]
    if keys[pygame.K_RIGHT]:
        player["x"] += player["speed"]
    if keys[pygame.K_UP]:
        player["y"] -= player["speed"]
    if keys[pygame.K_DOWN]:
        player["y"] += player["speed"]

    # Ensure the player stays within screen boundaries
    if player["x"] < 0:
        player["x"] = 0
    if player["x"] > screen.get_width() - player["width"]:
        player["x"] = screen.get_width() - player["width"]
    if player["y"] < 0:
        player["y"] = 0
    if player["y"] > screen.get_height() - player["height"]:
        player["y"] = screen.get_height() - player["height"]

    # Set the screen to black
    screen.fill(pygame.Color('black'))

    # Draw the player
    pygame.draw.rect(screen, pygame.Color('red'),
                        (player["x"], player["y"],
                         player["width"], player["height"])
                    )

    # Update display
    pygame.display.flip()

    # Wait for the end of frame at 60 fps
    clock.tick(60)
