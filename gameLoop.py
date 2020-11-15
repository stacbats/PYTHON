# game loop
# import eye
import pygame
import settings

# from eye import gameDisplay
# from eye import eye_image

def eye(x, y, gameDisplay, eye_image):      # eyeball
    gameDisplay.blit(eye_image, (x, y))

def gameplay(gameDisplay, eye_image):
    clock = pygame.time.Clock()

    x = (800 * 0.25) # position of eye X
    y = (600 * 0.4) # position of eye Y

    x_change = 0
    x = (800 * 0.25) # position of eye X
    y = (600 * 0.4) # position of eye Y

    x_change = 0

    exitGame = False

    while exitGame == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:# checking for key press left
                    x_change = -5
                elif event.key == pygame.K_RIGHT:# checking for key press right
                    x_change = 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(settings.BLACK)
        eye(x, y, gameDisplay, eye_image)

        pygame.display.update()
        clock.tick(60)
