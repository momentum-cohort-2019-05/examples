import random


def make_vin():
    valid_chars = ["A", "B", "C", "1", "2", "3"]
    return "".join([random.choice(valid_chars) for _ in range(20)])


class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.vin = make_vin()
