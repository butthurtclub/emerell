__author__ = 'emerell'
from math import hypot
from point import *

__all__ = (
    'Car',
)

class Car:
    def __init__(self, capacity=60, consumption=0.6, location=Point(0, 0), model='Mercedes'):
        self._fuel_capacity = capacity
        self._fuel_amount = 0
        self._location = location
        self._model = model
        self._fuel_consumption = consumption

    def __str__(self):
        return f'{self._model}: fuel amount {self._fuel_amount}, location {self._location}.'

    def __repr__(self):
        return f'{self._model}: fuel amount {self._fuel_amount}, location {self._location}.'

    def drive(self, destination):
        distance = hypot(destination.x - self._location.x, destination.y - self._location.y)
        fuel_needed = distance * self._fuel_consumption

        if fuel_needed > self._fuel_amount:
            raise Exception('Out of fuel!')

        self._fuel_amount -= fuel_needed
        self._location = destination

        return f'Car {self._model} travelled: {distance} miles. {self.fuel_amount} fuel left.'

    def refill(self, fuel):
        if fuel > self._fuel_capacity:
            raise Exception('Too much fuel!')

        self._fuel_amount = fuel

        return f'Car {self._model} refilled. {self._fuel_amount} fuel left. '


    @property
    def fuel_amount(self):
        return self._fuel_amount

    @property
    def fuel_capacity(self):
        return self._fuel_capacity

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @property
    def location(self):
        return self._location

    @property
    def model(self):
        return self._model
