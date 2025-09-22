import pygame
from .debugText import DebugText

class DebugTextRenderer:
    def __init__(self) -> None:
        self.display = pygame.display.get_surface()
        self.font = pygame.font.SysFont(None, 25)
        self.cache_texts = pygame.sprite.Group()

    def render(self, text: str, pos: pygame.Vector2, color: str | tuple[int, int, int] = "white", bg_color: str | tuple[int, int, int] = "yellow") -> None:
        rendered_text = self.font.render(text, True, color)
        debug_text = DebugText(rendered_text, pos, bg_color)
        self.cache_texts.add(debug_text)

        debug_text.draw(self.display)
                
    def draw_cache(self) -> None:
        for text in self.cache_texts.sprites():
            text.draw(self.display)

    def clear(self) -> None:
        for text in self.cache_texts.sprites():
            text.kill()