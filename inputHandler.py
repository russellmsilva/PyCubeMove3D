import pygame


# This function handles keyboard input to move the character. Character movement
# is frame-based, and each key press moves the character by 0.1 units per frame.
def handle_input(character):
    keys = pygame.key.get_pressed()  # Get the current state of all keys
    if keys[pygame.K_w]:  # Move forward
        character.move(0, 0, -0.1)
    if keys[pygame.K_s]:  # Move backward
        character.move(0, 0, 0.1)
    if keys[pygame.K_a]:  # Move left
        character.move(-0.1, 0, 0)
    if keys[pygame.K_d]:  # Move right
        character.move(0.1, 0, 0)
    if keys[pygame.K_SPACE]:  # Move up
        character.move(0, 0.1, 0)
    if keys[pygame.K_LSHIFT]:  # Move down
        character.move(0, -0.1, 0)
