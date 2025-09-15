import pygame


class Mouse:
    def __init__(self) -> None:
        self.position: pygame.Vector2 = None
        self.update()
    
    def update(self) -> None:
        pygame.Vector2(pygame.mouse.get_pos())
    
    def rect_collide(self, rect: pygame.Rect) -> bool:
        if self.position is None:
            return False
        return rect.collidepoint(self.position)
    