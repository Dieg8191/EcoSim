import pygame
from pygame import Vector2


class Entity(pygame.sprite.Sprite):
    def __init__(self, group: pygame.sprite.Group = None, pos: Vector2 = None) -> None:
        super().__init__(group)
        self.name = "Entity"

        # Basic attributes
        self.health = 100
        self.energy = 100
        self.hunger = 0
        self.thirst = 0
        self.age = 0 # in ticks
        self.speed = 50 # pixels per second

        if pos is None:
            self.position = Vector2(0, 0)
        else:
            self.position = Vector2(pos.x, pos.y)

        self.size = 20 # radius for circular representation
        self.image = pygame.Surface((self.size * 2, self.size * 2))
        self.image.set_colorkey((0, 0, 0)) # Set black as transparent
        pygame.draw.circle(self.image, "green", (self.size, self.size), self.size) # Green circle

        self.rect = self.image.get_rect(topleft=self.position)

    def update(self, **kwargs) -> None:
        # Update entity age
        dt = kwargs.get("dt", 0)
        self.age += dt

        # update rect position
        self.rect.topleft = self.position
        