from dataclasses import dataclass
from datetime import date

# Esta clase busca amntener los principios de la arquitectura limpia donde se mantiene una independencia entre
# los distintos componentes del sistema.
# Aqu[i se declaran las variables cables del mercado de valores.

class market_data:
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int
    pass