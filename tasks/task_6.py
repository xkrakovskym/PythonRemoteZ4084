"""
1. Vytvorte rozhranie Observer (pozorovateľ):
• Deklarujte metódu update(player), ktorá prijme aktuálny stav hráča a vykoná zodpovedajúcu akciu.

2. Vytvorte triedu Player (hráč):
• Obsahuje atribúty health a energy.
• Má metódy na zmenu health a energy.
• Implementuje správu pozorovateľov (add_observer, remove_observer) a notifikáciu pozorovateľov (notify_observers).

3. Vytvorte pozorovateľov (Observers):
• Liečiteľ (Healer): Sleduje zdravie hráča a ak klesne pod 50, automaticky zvýši zdravie o 10 bodov.
• Správca energie (Energy Manager): Sleduje energiu hráča a ak klesne pod 30, zobrazí varovanie.

4. Simulujte zmeny:
• Zmeňte stav hráča (zdravie, energiu) a sledujte, ako pozorovatelia reagujú.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, player):
        pass


class Player:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        self.observers = []

    def add_observer(self, observer):
        pass

    def remove_observer(self, observer):
        pass

    def notify_observers(self):
        pass

    def change_health(self, value):
        pass

    def change_energy(self, value):
        pass


class Healer(Observer):
    def update(self, player):
        pass


class EnergyManager(Observer):
    def update(self, player):
        pass

def main():
    player = Player(health=100, energy=100)
    healer = Healer()
    energy_manager = EnergyManager()

if __name__ == "__main__":
    main()