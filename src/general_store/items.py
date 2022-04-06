


import enum


class Wagon():

    def __init__(self) -> None:
        pass

class Ox():
    def __init__(self) -> None:
        pass

class RationSupply():
    def __init__(self) -> None:
        pass

class Gun():

    def __init__(self) -> None:
        pass

class AmmoBox():
    def __init__(self) -> None:
        self.percentage_remaining = 100

class Compass():
    class Directions(enum.Enum):
        
        W = "W"
        E = "E"
        N = "N"
        S = "S"

        NW = "NW"
        NE = "NE"
        SW = "SW"
        SE = "SE"

    def __init__(self) -> None:
        self.direction_facing:Compass.Directions = Compass.Directions.W

compass = Compass()
print(compass.direction_facing.value)
compass.direction_facing = Compass.Directions.NE
