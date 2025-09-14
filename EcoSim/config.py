from dataclasses import dataclass

@dataclass
class Config:
    fps: int = 60
    width: int = 800
    height: int = 600
    window_title: str = "EcoSim"
    tick_rate: float = 1/24  # Simulation tick rate in seconds
    

