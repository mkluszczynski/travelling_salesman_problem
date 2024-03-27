from random import choices

from src.AntDecisionItem import AntDecisionItem
from src.Path import Path
from src.PathService import PathService
from src.City import City


class Ant:

    path_service: PathService

    start_city: City
    current_city: City
    visited_cites: list[City]
    shortest_path: float

    def __init__(
        self,
        path_service: PathService,
        start_city: City
    ) -> None:
        self.path_service = path_service
        self.visited_cites = []
        self.start_city = start_city
        self.current_city = start_city
        self.visited_cites.append(self.current_city)
        self.shortest_path = 0

    def is_finished(self) -> bool:
        avalible_paths_len = len(self.path_service.get_avalible_paths(self.current_city, self.visited_cites))
        return avalible_paths_len == 0

    def move(self) -> None:
        decision_items = self.__get_decistion_items()
        ant_decision = self.__get_random_city(decision_items)
        self.current_city = ant_decision.city
        self.visited_cites.append(ant_decision.city)
        self.path_service.add_fermons(ant_decision.path, ant_decision.random_value)
        self.shortest_path += ant_decision.path.distance
        self.path_service.evapor_feromons()

    def go_back(self) -> None:
        go_back_path = self.path_service.get_connection_path(self.current_city, self.start_city)
        self.current_city = self.start_city
        self.shortest_path += go_back_path.distance
        self.visited_cites = [self.current_city]

    def __get_random_city(self, decistion_items: list[AntDecisionItem]) -> AntDecisionItem:
        random_values = []
        for item in decistion_items:
            random_values.append(item.random_value)

        return choices(decistion_items, random_values, k=1)[0]

    def __get_decistion_items(self) -> list[AntDecisionItem]:
        avalible_paths = self.path_service.get_avalible_paths(self.current_city, self.visited_cites)

        paths_div_value = self.__calculate_paths_div_value(avalible_paths)
        decision_items = []
        for path in avalible_paths:
            decision_items.append(
                AntDecisionItem(
                    path.destination,
                    path,
                    self.__calculate_path_value(path, paths_div_value)
                )
            )

        return decision_items


    def __calculate_path_value(self, path: Path, paths_div_value: float) -> float:
        fx = pow(path.feromon_strength, 1)
        hx = pow(1/path.distance, 2)
        random_value = (fx * hx) / paths_div_value
        return random_value

    def __calculate_paths_div_value(self, paths: list[Path]):
        div_value = 0

        for path in paths:
            div_value += (pow(path.feromon_strength, 1) * pow(1/path.distance, 2))

        return div_value
