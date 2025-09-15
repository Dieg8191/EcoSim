import pygame
from .entities.entity import Entity
from .support.timer import Timer
from .config import Config 
from .entities.animal import Animal
class Sim:
    def __init__(self) -> None:
        self.running = True
        self.clock = pygame.time.Clock()
        self.config = Config()

        self.display = pygame.display.get_surface()
        self.entities = pygame.sprite.Group()
        self.update_sprites = pygame.sprite.Group()

        self.ticks = 0
        self.speed_multiplier = 1.0 # 1 = Normal speed, play with it
        self.dt = 0
        self.get_dt = lambda: self.dt * self.speed_multiplier
        
        Animal(self.entities)
        self.tick_timer = Timer(self.get_dt, target_time=self.config.tick_rate, trigger=self.tick, repeat=True)

    def tick(self) -> None:
        self.ticks += 1

    def update(self) -> None:
        dt = self.get_dt()

        for entity in self.entities:
            entity.update(dt=dt)

    def draw(self) -> None:
        self.entities.draw(self.display)

    def run(self) -> str:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display.fill("gray")

            # Logic and rendering
            self.update()
            self.draw()

            #run tick timer
            self.tick_timer.update()

            pygame.display.flip()
            self.dt = self.clock.tick(self.config.fps) / 1000

        return "exit"
