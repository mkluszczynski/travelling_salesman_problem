from src.Ant import Ant
from src.CityService import CityService
from src.PathService import PathService


class AntService:

    city_service: CityService
    path_service: PathService

    ants: list[Ant]

    def __init__(
        self,
        city_service: CityService,
        path_service: PathService
    ) -> None:
        self.city_service = city_service
        self.path_service = path_service
        self.__init_ants()

    def start(self):
        for i in range(100):
            while(not(self.ants[0].is_finished())):
                for ant in self.ants:
                    ant.move()

            for ant in self.ants:
                ant.go_back()


    def __init_ants(self):
        ants = []
        for i in range(10):
            for city in self.city_service.cities:
                ants.append(Ant(self.path_service, city))

        self.ants = ants
