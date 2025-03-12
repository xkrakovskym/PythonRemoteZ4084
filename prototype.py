from abc import ABC, abstractmethod
from copy import deepcopy, copy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Enemy(Prototype):
    def __init__(self, name: str, health: float, attack_power: float, items: list):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.items = items

    def clone(self):
        return copy(self)

    def __str__(self):
        return f"Enemy(name={self.name}, health={self.health}, attack_power={self.attack_power})"


base_enemy = Enemy(name="Troll", health=100, attack_power=20)

enemy1 = base_enemy.clone()
enemy2 = base_enemy.clone()

enemy1.name = "Troll Warrior"
enemy2.attack_power = 40

print(enemy1)
print(enemy2)
