from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class Direction(Enum):
    UP = "up"
    DOWN = "down"
    NEUTRAL = "neutral"

@dataclass (frozen=true)
class Prediction:
    timestamp: datetime # momento en que se genera la prediccion
    horizon: int # horizonte de la prediccion - que tan lejos en el futuro aplica
    direction: Direction # decision del modelo hacia donde va el modelo
    confidence: float # nivel de confianza del modelo en esa prediccion
