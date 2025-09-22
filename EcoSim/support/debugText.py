import pygame


class DebugText(pygame.sprite.Sprite):
    def __init__(self, img: pygame.surface.Surface, pos: pygame.Vector2, bg_color: str | tuple[int, int, int] = None):
        super().__init__()
        self.image = img
        self.rect = img.get_rect(topleft=pos)

        if bg_color:
            bg = pygame.Surface((self.rect.w, self.rect.h))
            bg.fill(bg_color)
            bg.blit(self.image, (0, 0))
            self.image = bg

    def draw(self, display: pygame.surface.Surface):
        display.blit(self.image, self.rect)