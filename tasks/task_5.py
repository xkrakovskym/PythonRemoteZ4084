"""
	1.	Trieda CustomerQueue:
	•	Reprezentuje frontu zákazníkov.
	•	Obsahuje metódy:
	•	add_customer(name): Pridá zákazníka do fronty.
	•	__iter__(): Vráti inštanciu iterátora.
	2.	Iterátor CustomerQueueIterator:
	•	Umožňuje prístup ku každému zákazníkovi vo fronte.
	•	Obsahuje metódy:
	•	__iter__(): Vráti iterátor (samotný objekt).
	•	__next__(): Vráti ďalšieho zákazníka vo fronte. Ak je fronta prázdna, vyvolá výnimku StopIteration.
	3.	Použitie iterátora:
	•	Použite iterátor na prechod cez zákazníkov vo fronte a vypíšte ich mená (ako keby boli obslúžení).
"""

class CustomerQueue:
    def __init__(self):
        pass

    def add_customer(self, name):
        pass

    def __iter__(self):
        pass


class CustomerQueueIterator:
    def __init__(self, queue):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


# pridajte aspon 5tich zakaznikov a vypiste ich pomocou for cyklu