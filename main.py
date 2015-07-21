import pygame
import math

# PYGAME INITIALIZATION

pygame.init()


# (TEMPORARY) OPTION VARIABLES

HEIGHT = 720
WIDTH = int(HEIGHT / 9 * 16)

FPS = 60

DIMENSIONS = WIDTH, HEIGHT

NAME = 'IT'



white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (255,0,255)







# RENDERING

camX = camY = 0

zoom = 0

scale = 128


wood_floor = pygame.image.load("wood_floor.png")
wood_floor = pygame.transform.rotate(wood_floor, 45)
wood_floor = pygame.transform.smoothscale(wood_floor, (int(scale) + 1, int(scale * 0.5 + 1)))

def render():

    gameDisplay.fill(white)


    # for i in range(10):
    #     points = [[200 + 50 * i, 50 + 20 * i], [250 + 50 * i, 70 + 20 * i], [200 + 50 * i, 90 + 20 * i], [150 + 50 * i, 70 + 20 * i]]
    #     pygame.draw.polygon(gameDisplay, green, points)
    #     pygame.draw.lines(gameDisplay, red, True, points)

    for x in range(20):
        for y in range(20):
            gameDisplay.blit(wood_floor, (WIDTH/2 + x*scale/2 - y*scale/2, HEIGHT/4 + x*scale/4 + y*scale/4))

    pygame.display.flip()





# MAIN GAME LOOP

gameDisplay = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption(NAME)


pygame.display.update()


gameExit = False
clock = pygame.time.Clock()


while not gameExit:

    clock.tick(FPS)
    pygame.display.set_caption(NAME + " | FPS: " + str(int(clock.get_fps())) + " / " + str(FPS))


    for event in pygame.event.get():
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(event.button == 4):
                zoom += 1
        if(event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            gameExit = True



    render()


# QUIT AFTER EXITING GAME LOOP

pygame.quit()
quit()
