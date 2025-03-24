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
    def __init__(
        self, vehicle_type: str, speed: float, fuel: str, properties: list[str]
    ):
        self.vehicle_type = vehicle_type
        self.speed = speed
        self.fuel = fuel
        self.properties = properties

    def __str__(self):
        return ""

    def clone(self):
        return copy(self)


car_prototype = Vehicle("car", 120, "petrol", ["GPS", "self driving"])
moto_prototype = Vehicle("motorbike", 80, "petrol", ["Silencer", "honk"])

car1 = car_prototype.clone()
car2 = car_prototype.clone()

car1.properties.append("radio")
print(car1)


# vytvorenie zopar aut a motoriek
