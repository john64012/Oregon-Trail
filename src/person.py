

from __future__ import annotations

import random


class Person():
    def __init__(self, weight:int, money:int, strength:int) -> None:
        self.weight = weight
        self.money = money
        self.strength = strength

        self.fatigue = 0

    @classmethod
    def random(cls, weight_range:list[int], money_range:list[int],strength_range:list[int]):
        weight = random.randrange(*weight_range)
        money = random.randrange(*money_range)
        strength = random.randrange(*strength_range)
        return cls(weight,money,strength)




class PersonDefaultSettings():
    WEIGHT_RANGE = [100,150]
    STRENGTH_RANGE = [1,10]
    MONEY_RANGE = [25,150]
