import pygame
from .entities.entity import Entity

class Sim:
    def __init__(self, get_delta_time: callable) -> None:
        self.display = pygame.display.get_surface()
        self.entities = pygame.sprite.Group()
        self.update_sprites = pygame.sprite.Group()

        self.get_delta_time = get_delta_time
        
        Entity(self.entities)

    def update(self) -> None:
        dt = self.get_delta_time()

        for entity in self.entities:
            entity.update(delta_time=dt)

    def draw(self) -> None:
        self.entities.draw(self.display)
