from dataclasses import dataclass
from datetime import date

# Esta clase busca mantener los principios de la arquitectura limpia donde se mantiene una independencia entre
# los distintos componentes del sistema.
# Aqui se delcaran las variable pertenecientes a la vela (OHLCV)
@dataclass(frozen=true)
class market_data:
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int
    pass