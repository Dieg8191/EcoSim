import pygame
from .entity import Entity

class Plant(Entity):
    def __init__(self, group: pygame.sprite.Group = None, pos: pygame.Vector2 = None) -> None:
        super().__init__(group, pos)
        self.name = "Plant"
        self.draw_circle((34, 139, 34))  # Dark green color for plants

    def update(self, **kwargs) -> None:
        super().update(**kwargs)
        # Additional plant-specific update logic can go here