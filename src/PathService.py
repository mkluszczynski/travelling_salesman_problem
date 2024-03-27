from src.City import City
from src.CityService import CityService
from src.Path import Path


class PathService:

    city_service: CityService
    paths: list[Path]

    def __init__(self, city_service: CityService) -> None:
        self.city_service = city_service
        self.paths = []
        self.__init_paths()

    def __init_paths(self) -> None:
        for city in self.city_service.cities:
            for destination in self.city_service.cities:
                if city.alias == destination.alias: continue
                self.paths.append(Path(city, destination))

    def get_city_paths(self, city: City) -> list[Path]:
        city_paths = []
        for path in self.paths:
            if city.alias != path.start.alias: continue
            city_paths.append(path)

        return city_paths

    def get_connection_path(self, city_1: City, city_2: City):
        city_1_paths = self.get_city_paths(city_1)
        for path in city_1_paths:
            if(path.destination.alias != city_2.alias): continue;
            return path

        print(city_1.alias + " " + city_2.alias)
        raise Exception("[PathService] Connection path not found!")

    def get_avalible_paths(self, current_city: City, visited_cities: list[City]) -> list[Path]:
        city_paths = self.get_city_paths(current_city)

        avalible_paths = []
        for path in city_paths:
            if path.destination.alias in map(lambda city: city.alias, visited_cities): continue
            avalible_paths.append(path)

        return avalible_paths

    def add_fermons(self, path: Path, feromon_strenght: float):
        list(filter(lambda p: path.start.alias == p.start.alias and path.destination.alias == p.destination.alias, self.paths))[0].add_feromon(feromon_strenght)
        list(filter(lambda p: path.start.alias == p.destination.alias and path.destination.alias == p.start.alias, self.paths))[0].add_feromon(feromon_strenght)

    def evapor_feromons(self):

        for path in self.paths:
            path.evapor_fermon(0.1)
