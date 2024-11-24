import pygame
from constants.constants import SCREEN

def main():
    numpass, numfail = pygame.init()
    # game screen
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN.SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN.SCREEN_WIDTH, SCREEN.SCREEN_HEIGHT))
    
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

if __name__ == '__main__':
    main()
