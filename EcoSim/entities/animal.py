import pygame
from .entity import Entity

class Animal(Entity):
    def __init__(self, group: pygame.sprite.Group = None, pos: pygame.Vector2 = None) -> None:
        super().__init__(group, pos)
        self.name = "Animal"
        self.draw_circle((39, 245, 91))

    def update(self, **kwargs) -> None:
        super().update(**kwargs)
        # Additional animal-specific update logic can go here