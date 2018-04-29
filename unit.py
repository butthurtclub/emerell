__author__ = 'emerell'

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

        return f'{self._name} couner attack {enemy._name}!!!'

    @property
    def damage(self):
        return self._damage

    @property
    def hit_points(self):
        return self._hit_points

    @property
    def hit_points_limit(self):
        return self._hit_points_limit
