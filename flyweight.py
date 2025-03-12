import random


class Engine:
    instances = 0

    def __init__(self, identifier, volume, engine_type):
        Engine.instances += 1
        self._identifier = identifier
        self._volume = volume
        self._engine_type = engine_type

class Car:
    def __init__(self, producer, vin, model_name, engine):
        self._producer = producer
        self._vin = vin
        self._model_name = model_name
        self._engine = engine


class CarFactory:
    engines = [
        Engine("polo", 1.6, "PETROL"),
        Engine("golf", 2.0, "DIESEL")
    ]

    @staticmethod
    def crate_vw_polo(vin, engine_id):
        return Car("VW", vin, "Polo", CarFactory.engines[engine_id])

    @staticmethod
    def crate_vw_golf(vin, engine_id):
        return Car("VW", vin, "Golf", CarFactory.engines[engine_id])


def generate_vin():
    return random.randint(10000000,100000000)

car_factory = CarFactory()
produced_cars = []

for _ in range(10000):
    vin = generate_vin()
    engine_type_num = random.randint(0,1)
    produced_cars.append(car_factory.crate_vw_golf(vin, engine_type_num))

print(f"Produced {len(produced_cars)} car using {Engine.instances} engine objects")

