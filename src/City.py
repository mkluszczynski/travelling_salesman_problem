

class City:

    alias: str
    position: dict[str, int]

    def __init__(self, alias: str, position: dict[str, int]) -> None:
        self.alias = alias
        self.position = position
