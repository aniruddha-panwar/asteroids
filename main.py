import pygame
from constants.constants import SCREEN
from player import Player

def main():
    numpass, numfail = pygame.init()
    # game screen
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN.SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN.SCREEN_WIDTH, SCREEN.SCREEN_HEIGHT))

    # Decouple game speed from CPU speed
    # 60 max fps restriction
    clk = pygame.time.Clock()
    delta_time_sec = 0

    # Player groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)


    # init a player
    player = Player(
        x=SCREEN.SCREEN_WIDTH / 2,
        y=SCREEN.SCREEN_HEIGHT / 2
    )

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # draw player
        # player.update(delta_time_sec)
        # player.draw(screen=screen)
        # group actions
        # update
        for obj in updatable:
            obj.update(delta_time_sec)
        # draw
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        # pause game loop for 1/60 sec &
        # calc time since last tick
        delta_time_ms = clk.tick(60)
        delta_time_sec = delta_time_ms / 1000

if __name__ == '__main__':
    main()
