import pygame


class Mouse:
    def __init__(self, entities: pygame.sprite.Group) -> None:
        self.position: pygame.Vector2 = pygame.Vector2(pygame.mouse.get_pos())
        self.entities = entities

    def get_position(self) -> pygame.Vector2:
        return pygame.Vector2(self.position)

    def get_hovered_entity(self) -> pygame.sprite.Sprite | None:
        for e in self.entities.sprites():
            if self.rect_collide(e.rect):
                return e
        return None
    
    def update(self) -> None:
        x, y = pygame.mouse.get_pos()
        self.position.x = x
        self.position.y = y
    
    def rect_collide(self, rect: pygame.Rect) -> bool:
        if self.position is None:
            return False
        return rect.collidepoint(self.position.x, self.position.y)
    