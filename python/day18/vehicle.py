from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike starts using Self Start")

class ElectricCar(Vehicle):
    def start(self):
        print("Electric Car starts silently.")

bike = Bike()
electric = ElectricCar()
bike.start()
electric.start()
