from dataclasses import dataclass


@dataclass
class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    GRAY = (128, 128, 128)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    BROWN = (165, 42, 42)
    PINK = (255, 192, 203)
    LIGHT_GRAY = (211, 211, 211)
    DARK_GRAY = (169, 169, 169)
    LIGHT_BLUE = (173, 216, 230)
    DARK_BLUE = (0, 0, 139)
    LIGHT_GREEN = (144, 238, 144)
    DARK_GREEN = (0, 100, 0)
    LIGHT_RED = (255, 182, 193)
    DARK_RED = (139, 0, 0)
    TRANSPARENT = (0, 0, 0, 0)
    LIGHT_YELLOW = (255, 255, 224)
