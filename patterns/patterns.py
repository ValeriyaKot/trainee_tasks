class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def singleton(cls):
    instance = {}

    def call_singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return call_singleton


@singleton
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{}, {}'.format(self.name, self.age)


class Number(Singleton):
    def __init__(self):
        self.number = 1


class Name(metaclass=MetaSingleton):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    liz = Person("liz", 12)
    andi = Person("Andi", 2)
    num_1 = Number()
    num_2 = Number()
    oro = Name('Oro')
    tom = Name('Tom')
    
    print(num_1 is num_2)
    print(liz is andi)
    print(liz)
    print(andi)
    print(oro is tom)
    print(oro.name)
    print(tom.name)
