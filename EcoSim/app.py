import pygame
from .sim import Sim
from .config import Config
from .support.timer import Timer
from sys import exit as sys_exit

class App:
    def __init__(self, width=800, height=600) -> None:
        # Initialize Pygame and set up the window
        pygame.init()
        pygame.font.init()
        self.config = Config()

        self.screen = pygame.display.set_mode((self.config.width, self.config.height))
        pygame.display.set_caption(self.config.window_title)

        self.sim = Sim()

    def run(self) -> None:
        command = "sim"
        running = True

        while running:
            match command:
                case "sim":
                    command = self.sim.run()
                case "menu":
                    raise NotImplementedError("Menu not implemented yet")
                case "exit":
                    running = False

        pygame.quit()
        sys_exit()
