import pygame

def debug_text(
        surface: pygame.Surface,
        text: str,
        pos: tuple[int, int],
        color: str | tuple[int] = "white",
        font_size: int = 25,
        bg_color: str | tuple[int, int, int] = None) -> None:
    
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, color)

    if bg_color is not None:
        text_rect = text_surface.get_rect(topleft=pos)
        pygame.draw.rect(surface, bg_color, text_rect)

    surface.blit(text_surface, pos)