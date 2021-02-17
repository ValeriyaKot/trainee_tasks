from datetime import datetime, date
from functools import wraps


class IntTypeCheckDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, arg):
        if type(arg) is int:
            return self.func(arg)
        else:
            print('TypeError')


def age_check_decorator(cls):
    class Wrapper(cls):
        def check_age(self):
            if self.age >= 18:
                return 'Adult'
            else:
                return 'AgeError'

    return Wrapper


class HashListDecorator:
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            string = ''
            for element in result:
                string += str(element)
            return hash(string)

        return wrapper


def write_date_of_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        today = date.today()
        return '{}.{}.{}'.format(today.day, today.month, today.year) + '\n' + result

    return wrapper


def measure_speed_of_func(func):
    def wrapper(number):
        start = datetime.now()
        func(number)
        end = datetime.now()
        speed = (end - start).total_seconds() * 1000
        return speed

    return wrapper


@measure_speed_of_func
@IntTypeCheckDecorator
def find_squares(number):
    i = 1
    squares_list = []
    while i ** 2 <= number:
        squares_list.append(i ** 2)
        i += 1
    return squares_list


@HashListDecorator('test')
def create_full_name(first_name, last_name):
    """Create full name"""
    return first_name + ' ' + last_name


@write_date_of_func
def greet(username):
    return 'Hello, ' + username


@age_check_decorator
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @write_date_of_func
    def get_person(self):
        return 'Name: {}, age: {}'.format(self.name, self.age)


if __name__ == '__main__':
    lena = Person('Lena', 12)

    print(find_squares(111))
    print(create_full_name('Lena', 'Twist'))
    print(create_full_name.__doc__)
    print(greet('Liz'))
    print(lena.get_person())
    print(lena.check_age())
