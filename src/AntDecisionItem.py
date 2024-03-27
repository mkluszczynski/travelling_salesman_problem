from dataclasses import dataclass

from src.City import City
from src.Path import Path


@dataclass
class AntDecisionItem:

    city: City
    path: Path
    random_value: float
