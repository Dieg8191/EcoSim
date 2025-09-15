import pygame

class DebugText:
    def __init__(self) -> None:
        self.display = pygame.display.get_surface()
        self.font = pygame.font.SysFont(None, 25)
        self.cache = {}

    def render_text(self, text: str, color: str | tuple[int, int, int] = "white") -> list[pygame.surface.Surface]:
        rendered_text = []

        for char in text:
            if not char in self.cache:
                rendered_char = self.font.render(char, True, color)
                self.cache[char] = rendered_char
            else:
                rendered_char = self.cache[char]

            rendered_text.append(rendered_char)

        return rendered_text
                
    def draw(
        self,
        text: str,
        pos: tuple[int, int] | pygame.Vector2,
        bg_color: str | tuple[int, int, int] | None = "black",
        font_color: str | tuple[int, int, int] = "white",
        padding: int = 4
    ) -> None:
        rendered_text = self.render_text(text, font_color)
        x, y = pos

        if bg_color:
            total_width = sum(char.get_width() for char in rendered_text)
            max_height = max(char.get_height() for char in rendered_text)
            rect = pygame.Rect(x, y, total_width + padding * 2, max_height + padding * 2)
            pygame.draw.rect(self.display, bg_color, rect)

        x_offset = x + padding
        y_offset = y + padding
        for char in rendered_text:
            char_rect = char.get_rect(topleft=(x_offset, y_offset))
            self.display.blit(char, char_rect)
            x_offset += char.get_width()
