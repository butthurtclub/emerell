__author__ = 'emerell'

import unittest
from point import Point

__all__ = (
    'Car',
)


class FuelError(Exception):
    """Basic exception for errors in car module"""
    pass


class OutOfFuelError(FuelError):
    """When fuel amount is equal to 0"""
    pass


class TooMuchFuelError(FuelError):
    """Fuel capacity is already full"""
    pass


class Car:
    """
    A class for car representing.
    The car has the following properties: fuel capacity, amount of fuel, fuel consumption, location and model.

    The location is defined as a point on the coordinate plane. (Use module point)
    The car can drive to another point, but the car will not go if it haven't enough fuel to drive.
    The car can be fueled if it has necessary capacity.

    Usage:
    >>> car = Car()
    >>>  print(car)
    Mercedes: fuel amount | location: 0 | (0.0, 0.0)
    >>> car.fuel_capacity
    60.0
    >>> car.fuel_consumption
    0.6
    >>> car2 = Car(50.0, 0.6, Point(2, 4), "BMW")
    >>>car2.model
    'BMW'
    >>>car.fuel_amount = 50
    Car BMW refilled. 50 fuel left.
    >>>car2.drive(x=3, y =4)
    Car BMW travelled: 1.0 miles. 49.4 fuel left.
    >>>car.fuel_amount = 70
     Car Mercedes refilled. 70 fuel left.
    >>>car.drive(Point(0, 1))
    Car Mercedes travelled: 1.0 miles. 49.4 fuel left.
    """

    def __init__(self, capacity=60.0, consumption=0.6, location=Point(0, 0), model='Mercedes'):
        """
        The initializer.

        :param capacity: fuel capacity. Possible values: integer, float.
        :type capacity: float
        :param consumption: fuel consumption. Possible values: integer, float.
        :type consumption: float
        :param location: location on coordinate plane. Possible values: Point(x, y).
        :type location: Point
        :param model: model of the car. Possible values: string.
        :type model: string
        """
        self._fuel_capacity = capacity
        self._fuel_amount = 0
        self._location = location
        self._model = model
        self._fuel_consumption = consumption

    def __str__(self):
        return f'{self._model}: fuel amount | location: {self._fuel_amount} | {self._location}'

    def drive(self, destination=None, **kwargs):
        """
        Car drives to point.

        :param destination: location to move.
        :type destination: Point.
        :param kwargs: use if you want to specify coordinates like this: car.drive(x=3, y =4).

        print local distance of the car and its fuel amount.
        :raise OutOfFuelError: If the car is out of fuel.
        """

        destination = destination or Point(**kwargs)

        local_distance = self._location.distance(destination)
        fuel_needed = local_distance * self._fuel_consumption

        if fuel_needed > self._fuel_amount:
            raise OutOfFuelError('Out of fuel!')

        self._fuel_amount -= fuel_needed
        self._location = destination

        print(f'Car {self._model} travelled: {local_distance} miles. {self.fuel_amount} fuel left.')

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

    @fuel_amount.setter
    def fuel_amount(self, fuel):
        """
        Car can be fueled here

        :param fuel: fuel you want to refill with
        :type fuel: float

        print car and its fuel amount
        :raise TooMuchFuelError: If the car tank is full
        """

        if fuel > self._fuel_capacity:
            raise TooMuchFuelError('Too much fuel!')

        self._fuel_amount = fuel

        print(f'Car {self._model} refilled. {self._fuel_amount} fuel left.')


class TestCar(unittest.TestCase):
    def test_init(self):
        car = Car(50.0, 0.6, Point(2, 4), "Name")
        self.assertEqual(car.model, "Name")
        self.assertEqual(car.location, Point(2, 4))
        self.assertEqual(car.fuel_consumption, 0.6)
        self.assertEqual(car.fuel_capacity, 50.0)
        self.assertEqual(car.fuel_amount, 0)

    def test_fuel_amount(self):
        mercedes = Car()
        bmw = Car(50.0, 0.6, Point(2, 4), "BMW")
        bad_car = Car(20.0, 0.5, Point(1, 4))
        mercedes.fuel_amount = 40.0
        self.assertEqual(mercedes.fuel_amount, 40.0)
        bmw.fuel_amount = 10
        self.assertEqual(bmw.fuel_amount, 10)

        with self.assertRaises(TooMuchFuelError):
            bad_car.fuel_amount = 30

    def test_drive(self):
        mercedes = Car()
        bmw = Car(50.0, 0.6, Point(0, 3), "BMW")

        with self.assertRaises(OutOfFuelError):
            mercedes.drive(Point(0, 2))
            bmw.drive(Point(3, 4))

        mercedes.fuel_amount = 50
        self.assertEqual(mercedes.drive(Point(0, 1)), None)
        self.assertEqual(mercedes.drive(x=1, y=1), None)

    def test_presentation(self):
        mercedes = Car()
        bmw = Car(50.0, 0.6, Point(2, 4), "BMW")

        self.assertEqual(str(mercedes), 'Mercedes: fuel amount | location: 0 | (0.0, 0.0)')
        self.assertEqual(str(bmw), 'BMW: fuel amount | location: 0 | (2.0, 4.0)')


if __name__ == '__main__':
    unittest.main()

