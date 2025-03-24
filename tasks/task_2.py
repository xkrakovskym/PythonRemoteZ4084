"""
Predstavte si scenár systému na objednávanie pizze, v ktorom si zákazníci môžu prispôsobiť pizzu výberom rôznych príloh,
a veľkosti pizze. Použite nástroj Pattern Builder a určitým spôsobom zapúzdrite dizajn pizze,
ktorý udržiava proces konštrukcie oddelený od reprezentácie, čo uľahčuje pridávanie nových možností bez úpravy existujúceho kódu.
"""


class Pizza:
    def __init__(self):
        self.topping: list
        self.dough = None
        self.size = None

    def __str__(self):
        return f"Pizza with {self.topping}, {self.dough} dough and size {self.size}."


class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    def build(self):
        return self._pizza


# skontrolujte ci ma pizza cesto a nejaku velkost
