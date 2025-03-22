import random
import pygame
from sys import exit 


def coinFlip(): # coinflip function, amend to display on screen
    headOrTail = random.randint(1,2)
    if headOrTail == 1:
        print("it is heads")
    else:
        print("it is tails")


user_score = 0
airborne = False

pygame.init() # initialises pygame
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
pygame.display.set_caption("I run; the wind blows me")
font = pygame.font.Font("graphicas/Pixeltype.ttf",35)

score_surface = font.render("Score :" + str(user_score),False,(0,0,0))
scoreRect = score_surface.get_rect(center = (400,40))

circleSurface = pygame.image.load("graphicas\slue-circle.png").convert_alpha()
circleSurface = pygame.transform.scale(circleSurface,(50,50))
circleRect  = circleSurface.get_rect(bottomleft=(600,300))

sky_surafce = pygame.image.load('graphicas\Sky.png').convert()
groundSurface = pygame.image.load("graphicas\ground.png").convert()

playerSurface = pygame.image.load("graphicas\squarePNG31.png").convert_alpha()
playerSurface = pygame.transform.scale(playerSurface,(100,100))
playerRect = playerSurface.get_rect(midtop = (100,200))
player_gravity = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # the quit event occurs when the x is pressed
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and airborne == False:
                player_gravity = -20
                airborne = True
       
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playerRect.collidepoint(event.pos):
                player_gravity = -20  


    screen.blit(sky_surafce,(0,0)) 
    screen.blit(groundSurface,(0,300))

    screen.blit(score_surface,scoreRect)
    screen.blit(circleSurface,circleRect)

    circleRect.x -= 5

    if circleRect.right == 0: 
        circleRect.left = 800

    # Player
    player_gravity += 1
    playerRect.bottom += player_gravity
    if playerRect.bottom >= 300:
        playerRect.bottom = 300
        airborne = False
    
    screen.blit(playerSurface,playerRect)

    # collision
    if circleRect.colliderect(playerRect):
        pygame.quit()
        exit()

    if playerRect.colliderect(circleRect):
        print("we colliding fr")

    
    pygame.display.update() # updates to any changes we have made
    clock.tick(60)