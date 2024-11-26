from circleshape import CircleShape
import pygame
from constants.constants import ASTEROIDSTATS
from random import uniform
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "brown",
            self.position,
            self.radius,
            2
        )

    def update(self, dt):
        self.position += (self.velocity*dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROIDSTATS.ASTEROID_MIN_RADIUS:
            return
        # Spawn 2 new children asteroids
        # children will split and move between 20-50 degrees from original path
        split_children_angle = uniform(20,50)
        child_vector1 = self.velocity.rotate(split_children_angle)
        child_vector2 = self.velocity.rotate(-split_children_angle)
        child_radius = self.radius - ASTEROIDSTATS.ASTEROID_MIN_RADIUS
        child_asteroid1 = Asteroid(self.position.x, self.position.y, child_radius)
        child_asteroid1.velocity = child_vector1 * 1.2
        child_asteroid2 = Asteroid(self.position.x, self.position.y, child_radius)
        child_asteroid2.velocity = child_vector2 * 1.2


