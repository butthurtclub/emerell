__author__ = 'emerell'

import unittest

__all__ = (
    'Unit',
)


class UnitIsDeadError(Exception):
    """Unit hasn't hit points"""
    pass


class Unit:
    """
    A class for unit representing.
    The unit has the following properties: hit points limit, total hit points, damage, name of unit.

    Each unit can deal damage or restore a certain number of hit points.
    A unit can attack and counter attack another unit.

    Usage:
    >>> unit = Unit("Barbarian", 200, 20)
    >>>unit2 = Unit("Knight", 180, 25)
    >>>  print(unit)
    Barbarian: hp - 200; dmg - 20
    >>> unit.hit_points_limit
    200
    >>> print(unit2)
    Knight: hp - 180; dmg - 25
    >>> unit.attack(unit2)
    Barbarian attack Knight!!!
    >>>unit2.hit_points
    160
    >>>unit.counter_attack(unit2)
    Barbarian counter attack Knight!!!
    >>>unit2.hit_points
     120
    >>>unit2.take_damage(40)
    >>>unit2.hit_points
     80
    """

    def __init__(self, name, hp, dmg):
        """
        The initializer.

        :param name: name of unit. Possible values: string.
        :type name: string
        :param hp: total hit points. Possible values: integer, float.
        :type hp: integer, float
        :param dmg: damage. Possible values: integer, float.
        :type dmg: integer, float
         """
        self._name = name
        self._hit_points = hp
        self._hit_points_limit = hp
        self._damage = dmg

    def __str__(self):
        return f'{self.name}: hp - {self.hit_points}; dmg - {self.damage}'

    def _ensure_is_alive(self):
        """
        Check if the unit is alive.

        :raise: UnitIsDeadError: If the unit hasn't any hit points.
        """
        if self._hit_points == 0:
            raise UnitIsDeadError("Unit is dead")

    def take_damage(self, dmg):
        """
        Deals damage to a unit.

        :param dmg: the number of damage.
        :type dmg: integer, float
        :raise: UnitIsDeadError: If the number of hit points is less than the number of damage.

        """
        self._ensure_is_alive()

        if dmg > self._hit_points:
            raise UnitIsDeadError("Unit is dead")
        else:
            self._hit_points -= dmg

    def attack(self, enemy):
        """
        Attack the enemy unit.

        After the attack, the number of hit points of the enemy will decrease
        by the number of damage of the attacking unit.

        :param enemy: enemy unit.
        :type enemy: Unit
        """
        self._ensure_is_alive()

        enemy.take_damage(self._damage)

        print(f'{self._name} attack {enemy.name}!!!')

    def counter_attack(self, enemy):
        """
        Counter attack the enemy unit.

        After the counter attack, the number of hit points of the enemy will decrease
        by the number of damage of the attacking unit increased by 2 times.

        :param enemy: enemy unit.
        :type enemy: Unit
        """
        self._ensure_is_alive()

        enemy.take_damage(self._damage*2)

        print(f'{self._name} counter attack {enemy.name}!!!')

    @property
    def damage(self):
        return self._damage

    @property
    def name(self):
        return self._name

    @property
    def hit_points(self):
        return self._hit_points

    @property
    def hit_points_limit(self):
        return self._hit_points_limit

    @hit_points.setter
    def hit_points(self, hp):
        """
        Add hit point to the unit.
        You can't add hit points if their number is higher than limit.

        :param hp: the number of hit points you'd like to add

        """
        self._ensure_is_alive()

        new_hit_points = self._hit_points + hp

        if new_hit_points > self._hit_points_limit:
            self._hit_points = self._hit_points_limit
        else:
            self._hit_points = new_hit_points


class TestUnit(unittest.TestCase):
    def test_init(self):
        barbarian = Unit("Barbarian", 200, 20)
        knight = Unit("Knight", 180, 25)
        self.assertEqual(barbarian.name, 'Barbarian')
        self.assertEqual(knight.name, "Knight")
        self.assertEqual(barbarian.hit_points, 200)
        self.assertEqual(knight.hit_points, 180)
        self.assertEqual(barbarian.hit_points_limit, 200)
        self.assertEqual(knight.hit_points_limit, 180)
        self.assertEqual(barbarian.damage, 20)
        self.assertEqual(knight.damage, 25)

    def test_ensure_is_alive(self):
        barbarian = Unit("Barbarian", 0, 20)
        knight = Unit("Knight", 180, 25)

        self.assertEqual(knight._ensure_is_alive(), None)

        with self.assertRaises(UnitIsDeadError):
            barbarian._ensure_is_alive()

    def test_add_hit_points(self):
        barbarian = Unit("Barbarian", 0, 20)
        knight = Unit("Knight", 180, 25)

        self.assertEqual(barbarian.hit_points, 0)

        with self.assertRaises(UnitIsDeadError):
            barbarian.hit_points = 30

        self.assertEqual(knight.hit_points, 180)
        knight.hit_points = 10
        self.assertEqual(knight.hit_points, 180)

        knight.take_damage(50)
        knight.hit_points = 30
        self.assertEqual(knight.hit_points, 160)

    def test_take_damage(self):
        barbarian = Unit("Barbarian", 0, 20)
        knight = Unit("Knight", 180, 25)

        with self.assertRaises(UnitIsDeadError):
            barbarian.take_damage(30)

        knight.take_damage(50)
        self.assertEqual(knight.hit_points, 130)

        with self.assertRaises(UnitIsDeadError):
            knight.take_damage(160)

    def test_attack(self):
        bad_unit = Unit("Bad Unit", 0, 20)
        knight = Unit("Knight", 180, 25)
        barbarian = Unit("Barbarian", 100, 20)

        with self.assertRaises(UnitIsDeadError):
            bad_unit.attack(knight)

        self.assertEqual(knight.attack(barbarian), None)
        self.assertEqual(knight.hit_points, 180)
        self.assertEqual(barbarian.hit_points, 75)

        self.assertEqual(barbarian.attack(knight), None)
        self.assertEqual(barbarian.hit_points, 75)
        self.assertEqual(knight.hit_points, 160)

    def test_counter_attack(self):
        bad_unit = Unit("Bad Unit", 0, 20)
        knight = Unit("Knight", 180, 25)
        barbarian = Unit("Barbarian", 100, 20)

        with self.assertRaises(UnitIsDeadError):
            bad_unit.counter_attack(knight)

        self.assertEqual(knight.counter_attack(barbarian), None)
        self.assertEqual(knight.hit_points, 180)
        self.assertEqual(barbarian.hit_points, 50)

        self.assertEqual(barbarian.counter_attack(knight),None)
        self.assertEqual(barbarian.hit_points, 50)
        self.assertEqual(knight.hit_points, 140)

    def test_presentation(self):
        knight = Unit("Knight", 180, 25)
        barbarian = Unit("Barbarian", 100, 20)

        self.assertEqual(str(knight), 'Knight: hp - 180; dmg - 25')
        self.assertEqual(str(barbarian), 'Barbarian: hp - 100; dmg - 20')


if __name__ == '__main__':
    unittest.main()