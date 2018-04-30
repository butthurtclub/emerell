__author__ = 'emerell'

import unittest

__all__ = (
    'Unit',
)


class Unit:
    def __init__(self, name, hp, dmg):
        self._name = name
        self._hit_points = hp
        self._hit_points_limit = hp
        self._damage = dmg

    def __repr__(self):
        return f'{self._name} has {self._hit_points} hitPoints | hitPointLimit:{self._hit_points_limit} |; ' \
               f'Damage: {self._damage}'

    def __str__(self):
        return f'{self.name}: hp - {self.hit_points}; dmg - {self.damage}'

    def _ensure_is_alive(self):
        if self._hit_points == 0:
            raise Exception("Unit is dead")

    def add_hit_points(self, hp):
        self._ensure_is_alive()

        new_hit_points = self._hit_points + hp

        if new_hit_points > self._hit_points_limit:
            self._hit_points = self._hit_points_limit
        else:
            self._hit_points = new_hit_points

    def take_damage(self, dmg):
        self._ensure_is_alive()

        if dmg > self._hit_points:
            raise Exception("Unit is dead")
        else:
            self._hit_points -= dmg

    def attack(self, enemy):
        self._ensure_is_alive()

        enemy.take_damage(self._damage)

        return f'{self._name} attack {enemy._name}!!!'

    def counter_attack(self, enemy):
        self._ensure_is_alive()

        enemy.take_damage(self._damage*2)

        return f'{self._name} counter attack {enemy._name}!!!'

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

        with self.assertRaises(Exception):
            barbarian._ensure_is_alive()

    def test_add_hit_points(self):
        barbarian = Unit("Barbarian", 0, 20)
        knight = Unit("Knight", 180, 25)

        self.assertEqual(barbarian.hit_points, 0)

        with self.assertRaises(Exception):
            barbarian.add_hit_points(30)

        self.assertEqual(knight.hit_points, 180)
        knight.add_hit_points(10)
        self.assertEqual(knight.hit_points, 180)

        knight.take_damage(50)
        knight.add_hit_points(30)
        self.assertEqual(knight.hit_points, 160)

    def test_take_damage(self):
        barbarian = Unit("Barbarian", 0, 20)
        knight = Unit("Knight", 180, 25)

        with self.assertRaises(Exception):
            barbarian.take_damage(30)

        knight.take_damage(50)
        self.assertEqual(knight.hit_points, 130)

        with self.assertRaises(Exception):
            knight.take_damage(160)

    def test_attack(self):
        bad_unit = Unit("Bad Unit", 0, 20)
        knight = Unit("Knight", 180, 25)
        barbarian = Unit("Barbarian", 100, 20)

        with self.assertRaises(Exception):
            bad_unit.attack(knight)

        self.assertEqual(knight.attack(barbarian), 'Knight attack Barbarian!!!')
        self.assertEqual(knight.hit_points, 180)
        self.assertEqual(barbarian.hit_points, 75)

        self.assertEqual(barbarian.attack(knight), 'Barbarian attack Knight!!!')
        self.assertEqual(barbarian.hit_points, 75)
        self.assertEqual(knight.hit_points, 160)

    def test_counter_attack(self):
        bad_unit = Unit("Bad Unit", 0, 20)
        knight = Unit("Knight", 180, 25)
        barbarian = Unit("Barbarian", 100, 20)

        with self.assertRaises(Exception):
            bad_unit.counter_attack(knight)

        self.assertEqual(knight.counter_attack(barbarian), 'Knight counter attack Barbarian!!!')
        self.assertEqual(knight.hit_points, 180)
        self.assertEqual(barbarian.hit_points, 50)

        self.assertEqual(barbarian.counter_attack(knight), 'Barbarian counter attack Knight!!!')
        self.assertEqual(barbarian.hit_points, 50)
        self.assertEqual(knight.hit_points, 140)

    def test_presentation(self):
        knight = Unit("Knight", 180, 25)
        barbarian = Unit("Barbarian", 100, 20)

        self.assertEqual(str(knight), 'Knight: hp - 180; dmg - 25')
        self.assertEqual(repr(knight), 'Knight has 180 hitPoints | hitPointLimit:180 |; '
                                       'Damage: 25')

        self.assertEqual(str(barbarian), 'Barbarian: hp - 100; dmg - 20')
        self.assertEqual(repr(barbarian), 'Barbarian has 100 hitPoints | hitPointLimit:100 |;'
                                          ' Damage: 20')


if __name__ == '__main__':
    unittest.main()