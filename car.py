__author__ = 'emerell'

import unittest
from point import *

__all__ = (
    'Car',
)


class Car:
    def __init__(self, capacity=60.0, consumption=0.6, location=Point(0, 0), model='Mercedes'):
        self._fuel_capacity = capacity
        self._fuel_amount = 0
        self._location = location
        self._model = model
        self._fuel_consumption = consumption

    def __str__(self):
        return f'{self._model}: fuel amount | location: {self._fuel_amount} | {self._location}'

    def __repr__(self):
        return f'{self._model}: fuel amount {self._fuel_amount}, location {self._location}.'

    def drive(self, destination):
        local_distance = self._location.distance(destination)
        fuel_needed = local_distance * self._fuel_consumption

        if fuel_needed > self._fuel_amount:
            raise Exception('Out of fuel!')

        self._fuel_amount -= fuel_needed
        self._location = destination

        return f'Car {self._model} travelled: {local_distance} miles. {self.fuel_amount} fuel left.'

    def refill(self, fuel):
        if fuel > self._fuel_capacity:
            raise Exception('Too much fuel!')

        self._fuel_amount = fuel

        return f'Car {self._model} refilled. {self._fuel_amount} fuel left.'

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


class TestCar(unittest.TestCase):
    def test_init(self):
        car = Car(50.0, 0.6, Point(2, 4), "Name")
        self.assertEqual(car.model, "Name")
        self.assertEqual(car.location, Point(2, 4))
        self.assertEqual(car.fuel_consumption, 0.6)
        self.assertEqual(car.fuel_capacity, 50.0)
        self.assertEqual(car.fuel_amount, 0)

    def test_refill(self):
        mercedes = Car()
        bmw = Car(50.0, 0.6, Point(2, 4), "BMW")
        bad_car = Car(20.0, 0.5, Point(1, 4))
        self.assertEqual(mercedes.refill(40.0), 'Car Mercedes refilled. 40.0 fuel left.')
        self.assertEqual(bmw.refill(10), 'Car BMW refilled. 10 fuel left.')

        with self.assertRaises(Exception):
            bad_car.refill(30.0)

    def test_drive(self):
        mercedes = Car()
        bmw = Car(50.0, 0.6, Point(0, 3), "BMW")

        with self.assertRaises(Exception):
            mercedes.drive(Point(0, 2))
            bmw.drive(Point(3, 4))

        mercedes.refill(50)
        self.assertEqual(mercedes.drive(Point(0, 1)), 'Car Mercedes travelled: 1.0 miles. 49.4 fuel left.')

    def test_presentation(self):
        mercedes = Car()
        bmw = Car(50.0, 0.6, Point(2, 4), "BMW")

        self.assertEqual(str(mercedes), 'Mercedes: fuel amount | location: 0 | (0, 0)')
        self.assertEqual(repr(mercedes), 'Mercedes: fuel amount 0, location (0, 0).')

        self.assertEqual(str(bmw), 'BMW: fuel amount | location: 0 | (2, 4)')
        self.assertEqual(repr(bmw), 'BMW: fuel amount 0, location (2, 4).')


if __name__ == '__main__':
    unittest.main()