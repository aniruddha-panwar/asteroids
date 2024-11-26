from circleshape import CircleShape
from constants.constants import PLAYERPROP, BULLETPROP
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYERPROP.PLAYER_RADIUS)
        self.rotation = 0

    def _triangle(self):
        """
        Triangle hitbox for a circular player
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self._triangle(),
            2
        )

    def _rotate(self, delta_time_sec):
        self.rotation += PLAYERPROP.PLAYER_TURN_SPEED * delta_time_sec

    def update(self, delta_time_sec):
        keys = pygame.key.get_pressed()

        # rotate left
        if keys[pygame.K_a]:
            self._rotate(delta_time_sec=delta_time_sec)
        # rotate right
        if keys[pygame.K_d]:
            self._rotate(delta_time_sec=-1*delta_time_sec)
        # move forward
        if keys[pygame.K_w]:
            self._move(delta_time_sec=delta_time_sec)
        # move backward
        if keys[pygame.K_s]:
            self._move(delta_time_sec=-1*delta_time_sec)
        # take a shot
        if keys[pygame.K_SPACE]:
            self.shoot()

    def _move(self, delta_time_sec):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYERPROP.PLAYER_SPEED * delta_time_sec

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        shot.velocity = forward * PLAYERPROP.PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y, radius = BULLETPROP.SHOT_RADIUS):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "yellow",
            self.position,
            self.radius,
            2
        )

    def update(self, dt):
        self.position += (self.velocity*dt)