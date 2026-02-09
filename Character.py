
# Character Game 🎮

class Character:

    def __init__(self, name, power, game_time_minutes):
        self.name = name
        self.power = power
        self.game_time_minutes = game_time_minutes

    def get_game_time(self):
        return self.game_time_minutes

    def __eq__(self, other):
        # _mario == _luigi
        if isinstance(other, int | float):
            return self.power == other
        return self.power == other.power

    def __gt__(self, other):
        # _mario == _luigi
        if isinstance(other, int | float):
            return self.power > other
        return self.power > other.power

    def __ge__(self, other):
        # >
        # <
        # >=
        # return self > other or self == other
        return not self < other

    def __lt__(self, other):
        # _mario == _luigi
        if isinstance(other, int | float):
            return self.power < other
        return self.power < other.power

    # overloading , operator overloading +
    def __len__(self):
        return self.game_time_minutes

    def __str__(self):
        return f"[Character {self.name} {self.power}]"

    def __repr__(self):
        return f"Character('{self.name}', {self.power}, {self.game_time_minutes})"

    def __add__(self, other):
        self.power += other
        return self


_mario = Character("Mario", 80, 110)
_luigi = Character("Luigi", 70, 90)

print(f"{_mario.name} played {len(_mario)} minutes!")
print(f"{_mario.name} played {_mario.game_time_minutes} minutes!")
print(f"{_mario.name} played {_mario.get_game_time()} minutes!")
# [1,2,3].__len__()

# a1 = [1,2,3]
# a2 = [1,2,3]
# print(a1 == a2) True, why?

print('_mario == _luigi?', _mario == _luigi, _mario, _luigi)
_luigi.power = 80
print('_mario == _luigi?', _mario == _luigi, _mario, _luigi)
print('_mario == 80?', _mario == 80.0, _mario)
print('_mario > 70?', _mario > 70, _mario)
print('_mario < 70?', _mario < 70, _mario)
print('_mario > 70?', _mario > 70, _mario)
print('_mario >= 70?', _mario >= 70, _mario)
print('_mario >= 80?', _mario >= 80, _mario)
print('_mario >= 80?', _mario >= _luigi, _mario, _luigi)
_mario = _mario + 5
print(_mario)

print([_mario, _luigi, _mario])

_luigi = Character('Luigi', 80, 90)
