from dataclasses import dataclass
from datetime import date

class market_data:
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int
    pass