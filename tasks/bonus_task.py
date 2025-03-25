"""
Úloha: Strategy Pattern – Správanie nepriateľov v hre

Cieľ:

Implementujte rôzne stratégie útoku pre nepriateľov v jednoduchej RPG hre.
Každý typ nepriateľa (napr. Goblin, Kostlivec, Drak) by mal vedieť meniť
svoju útočnú stratégiu počas behu programu, bez potreby meniť samotnú
triedu Enemy.

Zadanie

V hre máte nepriateľov, ktorí používajú rôzne typy útokov:
    •	Goblin útočí na blízko
    •	Kostlivec strieľa šípy
    •	Drak dýcha oheň alebo kúzli

Každý nepriateľ by mal byť schopný zmeniť svoju stratégiu útoku počas hry
(napríklad keď získa nový predmet).

🔧 Požiadavky:
    1.	Vytvorte rozhranie AttackStrategy s metódou attack
    2.	Implementujte aspoň tri stratégie:
    •	MeleeAttack
    •	RangedAttack
    •	MagicAttack
    3.	Vytvorte triedu Enemy, ktorá:
    •	Má meno (napr. „Goblin“)
    •	Má aktuálnu attack_strategy
    •	Má metódu perform_attack(), ktorá volá aktuálnu stratégiu
    •	Má metódu set_strategy(strategy), ktorá umožňuje meniť správanie
    4.	Vytvorte jednoduchú simuláciu, ktorá:
    •	Vytvorí viacero nepriateľov s rôznymi stratégiami
    •	Zmení jednému nepriateľovi stratégiu počas behu
    •	Ukáže, že správanie sa zmenilo bez potreby meniť kód Enemy

Bonus
    •	Rozšírte o DefendStrategy
    •	Vytvorte triedu BattleManager, ktorá spustí viacero
        kôl a náhodne mení stratégie
"""

from abc import ABC, abstractmethod


class AttackStrategy(ABC):
    @abstractmethod
    def attack(self, enemy_name: str) -> None:
        pass


class MeleeAttack(AttackStrategy):
    def attack(self, enemy_name: str) -> None:
        pass


class RangedAttack(AttackStrategy):
    def attack(self, enemy_name: str) -> None:
        pass


class MagicAttack(AttackStrategy):
    def attack(self, enemy_name: str) -> None:
        pass


class Enemy:
    def __init__(self, name: str, strategy: AttackStrategy):
        self.name = name
        self.strategy = strategy

    def set_strategy(self, strategy: AttackStrategy) -> None:
        pass

    def perform_attack(self) -> None:
        pass


def main():
    goblin = Enemy("Goblin", MeleeAttack())
    skeleton = Enemy("Skeleton", RangedAttack())
    dragon = Enemy("Dragon", MagicAttack())

    goblin.perform_attack()
    skeleton.perform_attack()
    dragon.perform_attack()

    print("Goblin picks up a magic wand...")
    goblin.set_strategy(MagicAttack())
    goblin.perform_attack()


if __name__ == "__main__":
    main()
