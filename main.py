import pygame
import sys
from constants.constants import SCREEN
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

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
    # Asteroid groups
    asteroid_grp = pygame.sprite.Group()
    # Bullet/shot groups
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroid_grp, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    Player.containers = (updatable, drawable)

    # init asteroidfield
    asteroid_field = AsteroidField()

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
        # draw player
        # player.update(delta_time_sec)
        # player.draw(screen=screen)
        # group actions
        # update
        for obj in updatable:
            obj.update(delta_time_sec)

        for asteroid_item in asteroid_grp:
            for bullet in shots:
                if asteroid_item.collides_with(bullet):
                    bullet.kill()
                    asteroid_item.split()
            if asteroid_item.collides_with(player):
                sys.exit("Game over!")

        screen.fill("black")
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
