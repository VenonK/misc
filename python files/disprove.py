import pygame

def main():
    pygame.init()

    logo = pygame.image.load("+1000000 social credit.jpg") # change this
    pygame.display.set_icon(logo)
    pygame.display.set_caption("what the dog doing")

    screen = pygame.display.set_mode()

    running = True # initialises the loop

    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()

reminder = "https://www.pygame.org/wiki/tutorials"