from random import uniform


class Randomizer:
    def __init__(self, number_of_iterations):
        self.number_of_iterations = number_of_iterations
        self.random_number = uniform(0, 1)

    def __next__(self):
        if self.number_of_iterations > 0:
            self.number_of_iterations -= 1
            self.random_number = self.random_number + uniform(0, 1)
            return self.random_number
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    randomizer = Randomizer(10)
    for i in randomizer:
        print(i)
