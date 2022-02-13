class Dog:
    _happiness = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def human_age(self):
        return self.age * 7.3

    @property
    def happiness(self):
        return self._happiness

    @happiness.setter
    def happiness(self, value):
        if 0 <= value <= 100:
            self._happiness = value
        else:
            raise ValueError("Happiness must be between 0 ... 100")


jane = Dog("jane", 4)
jane.happiness = 100
print(jane.happiness)
