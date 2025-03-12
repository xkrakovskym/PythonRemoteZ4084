"""
	1.	Vytvorte triedu Vehicle, ktorá obsahuje nasledujúce vlastnosti:
	•	type (car, motorbike,..)
	•	speed
	•	fuel
	•	properties: list (self driving, gps, etc)
	2.	Implementujte metódu clone(), ktorá vytvorí kópiu inštancie Vehicle.
	3.	Pomocou prototypu vytvorte základné vozidlo a klonujte ho, pričom upravíte jeho vlastnosti (napr. zvýšite rýchlosť alebo zmeníte typ paliva).
	4.  Overte funkcionalitu copy a deepcopy na liste properties
"""

from copy import copy

class Vehicle:
    def __init__(self, vehicle_type: str, speed: float, fuel: str, properties: list[str]):
        pass

    def __str__(self):
        pass

    def clone(self):
        return copy(self)


car_prototype = Vehicle()
moto_prototype = Vehicle()


# vytvorenie zopar aut a motoriek
