from src.City import City


class Path:

    distance: float
    start: City
    destination: City
    feromon_strength: float

    def __init__(self, start_city: City, destination_city: City) -> None:
        self.start = start_city
        self.destination = destination_city
        self.feromon_strength = 1
        self.__calc_distance()



    def __calc_distance(self) -> None:
        x = self.start.position["x"] - self.destination.position["x"]
        y = self.start.position["y"] - self.destination.position["y"]

        distance = pow(x, 2) + pow(y, 2)
        distance = distance ** (1/2)

        self.distance = distance

    def add_feromon(self, feromon: float) -> None:
        self.feromon_strength += feromon


    def evapor_fermon(self, evapor_stregth: float) -> None:
        if self.feromon_strength - evapor_stregth < 0 : return
        self.feromon_strength -= evapor_stregth
