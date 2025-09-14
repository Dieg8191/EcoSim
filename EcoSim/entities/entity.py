import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, group: pygame.sprite.Group = None) -> None:
        super().__init__(group)
        self.name = "Entity"
        self.health = 100
        self.age = 0
        self.speed = 50 # pixels per second

        self.position = pygame.Vector2(0, 0)

        self.size = 10 # radius for circular representation
        self.image = pygame.Surface((self.size * 2, self.size * 2))
        self.image.fill((0, 255, 0)) # Green color
        self.rect = self.image.get_rect(center=self.position)

    def update(self, **kwargs) -> None:
        pass
        
