import pygame

pygame.init()
WINDOW_WIDTH , WINDOW_HEIGHT = 1280, 720
displaySurface = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT))
pygame.display.set_caption('Blew :p')
running = True

#surface
surf = pygame.Surface((100,200))


while running: 
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # draw the game
    displaySurface.fill('grey')
    displaySurface.blit(surf, (100,150))
    pygame.display.flip()


pygame.quit()
