import pygame
from pygame import Vector2
from abc import ABC, abstractmethod


class Entity(pygame.sprite.Sprite, ABC):
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

        self.set_circle(10, "blue")

    def set_circle(self, size: int, color: str | tuple[int]) -> None:
        self.image = pygame.Surface((size * 2, size * 2))
        self.rect = self.image.get_rect(topleft=self.position)

        pygame.draw.circle(self.image, color, (size, size), size)
        self.image.set_colorkey((0, 0, 0)) # Set black as transparent

    @abstractmethod
    def update(self, **kwargs) -> None:
        # Update entity age
        dt = kwargs.get("dt", 0)

        # update rect position
        self.rect.topleft = self.position

    def tick_update(self) -> None:
        # Update hunger and thirst over time
        self.hunger += 0.1
        self.thirst += 0.1

        # Decrease health if hunger or thirst exceed certain thresholds
        if self.hunger > 100:
            self.health -= 1
        if self.thirst > 100:
            self.health -= 1
        
        if self.health <= 0:
            self.kill()
