import pygame
from .sim import Sim
from .config import Config
from .support.timer import Timer

class App:
    def __init__(self, width=800, height=600) -> None:
        # Initialize Pygame and set up the window
        pygame.init()
        pygame.font.init()
        self.config = Config()

        self.screen = pygame.display.set_mode((self.config.width, self.config.height))
        pygame.display.set_caption(self.config.window_title)

        self.clock = pygame.time.Clock()
        self.running = True
        self.delta_time = 0
        self.tick_count = 0

        self.sim = Sim(self.get_delta_time)

        self.tick_timer = Timer(self.get_delta_time, target_time=self.config.tick_rate, trigger=self.tick, repeat=True)
        self.speed_multiplier = 1 # 1 = Normal speed, play with it

    def get_delta_time(self) -> float:
        return self.delta_time * self.speed_multiplier
    
    def tick(self) -> None:
        self.tick_count += 1
        print(f"Tick: {self.tick_count}")

    def run(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))  # Clear screen with black

            # Logic and rendering
            self.sim.update()
            self.sim.draw()

            #run tick timer
            self.tick_timer.update()

            pygame.display.flip()
            self.delta_time = self.clock.tick(self.config.fps) / 1000  # Limit to 60 FPS and get delta time in seconds

        pygame.quit()