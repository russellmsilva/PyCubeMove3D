import pygame

def handle_input(character):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        character.move(0, 0, -0.1)
    if keys[pygame.K_s]:
    	character.move(0, 0, 0.1)        
    if keys[pygame.K_a]:
        character.move(-0.1, 0, 0)
    if keys[pygame.K_d]:
        character.move(0.1, 0, 0)
