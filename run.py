import pygame
pygame.init()
sc = pygame.display.set_mode((500,500))
run = True
while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
