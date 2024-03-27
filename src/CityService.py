from src.Path import Path
from src.City import City


class CityService:

    cities: list[City]
    paths: list[Path]

    def __init__(self, cities: list[City]) -> None:
        self.cities = cities
        self.paths = []

    def get_remaning_cities(self, visited_cities: list[City]) -> list[City]:
        return list(set(self.cities) - set(visited_cities))
