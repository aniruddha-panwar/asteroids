from circleshape import CircleShape
from constants.constants import SHAPE, TURNSPEED, MOVESPEED
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHAPE.PLAYER_RADIUS)
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
        self.rotation += TURNSPEED.PLAYER_TURN_SPEED * delta_time_sec

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

    def _move(self, delta_time_sec):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * MOVESPEED.PLAYER_SPEED * delta_time_sec