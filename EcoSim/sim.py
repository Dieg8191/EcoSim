import pygame
from .entities.entity import Entity
from .support.timer import Timer
from .config import Config 
from .entities.animal import Animal
from .entities.plant import Plant
from .support.mouse import Mouse
from .support.debugText import debug_text


class Sim:
    def __init__(self) -> None:
        self.running = True
        self.debug = True
        self.clock = pygame.time.Clock()
        self.config = Config()

        self.display = pygame.display.get_surface()
        self.entities = pygame.sprite.Group()
        self.update_sprites = pygame.sprite.Group()
        self.mouse = Mouse()

        self.ticks = 0
        self.speed_multiplier = 1.0 # 1 = Normal speed, play with it
        self.dt = 0
        self.get_dt = lambda: self.dt * self.speed_multiplier
        
        Animal(self.entities)
        Plant(self.entities, pygame.Vector2(100, 100))

        self.tick_timer = Timer(self.get_dt, target_time=self.config.tick_rate, trigger=self.tick, repeat=True)

    def tick(self) -> None:
        self.ticks += 1

    def update(self) -> None:
        dt = self.get_dt()

        for entity in self.entities:
            entity.update(dt=dt)

    def draw(self) -> None:
        self.entities.draw(self.display)

    def debug_info(self) -> None:
        debug_text(self.display, f"FPS: {self.clock.get_fps():.0f}", (10, 10), bg_color=(0, 0, 0, 150))

    def run(self) -> str:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_F3:
                        self.debug = not self.debug

            self.display.fill("gray")

            # Logic and rendering
            self.update()
            self.draw()

            # show debug info
            if self.debug: self.debug_info()

            #run tick timer
            self.tick_timer.update()
            self.mouse.update()

            pygame.display.flip()
            self.dt = self.clock.tick(self.config.fps) / 1000

        return "exit"
