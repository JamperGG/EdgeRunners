class Person:
    def __init__(self, name, age):
        self.name = name           # Публічний атрибут
        self._age = age           # Захищений атрибут
        self.__salary = 0         # Приватний атрибут

    @property
    def age(self):
        """Властивість для доступу до захищеного атрибута"""
        return self._age

    @age.setter
    def age(self, value):
        """Властивість для зміни захищеного атрибута"""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @property
    def salary(self):
        """Властивість для доступу до приватного атрибута"""
        return self.__salary
