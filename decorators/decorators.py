from datetime import datetime
from functools import wraps


class IntTypeCheckDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, arg):
        if type(arg) is int:
            return self.func(arg)
        else:
            print('TypeError')


class HashListDecorator:
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            string = ''
            for element in result:
                string += str(element)
            return hash(string)

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
def create_full_name(*args):
    """Create full name"""
    return str(args[0]) + ' ' + str(args[1])


print(find_squares(111))
print(create_full_name('Lena', 'Twist'))
print(create_full_name.__doc__)
