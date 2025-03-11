class Bird:
    def fly(self):
        return "I am flying!"


class Sparrow(Bird):
    def fly(self):
        return "I am a sparrow, and I am flying!"


class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches cannot fly!")

"""
Bad example:
bird1 = Bird()
bird2 = Ostrich()

group_of_birds = [bird1, bird2]

for bird in group_of_birds:
    bird.fly()
"""

from abc import ABC, abstractmethod


class CorrectBird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(CorrectBird):
    def move(self):
        return "I am flying!"


class NonFlyingBird(CorrectBird):
    def move(self):
        return "I am walking"


class GoodSparrow(FlyingBird):
    pass


class GoodOstrich(NonFlyingBird):
    pass


bird1 = GoodSparrow()
bird2 = GoodOstrich()

group_of_birds = [bird1, bird2]

for bird in group_of_birds:
    bird.move()