import pygame

class CircleShape(pygame.sprite.Sprite):

    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(x,y)
        self.radius = radius

    def draw(self, screen):
        # override using subclass
        pass

    def update(self, dt):
        # sub-classes must override
        pass