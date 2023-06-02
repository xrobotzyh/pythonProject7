import itertools
import csv


class Action:
    def __init__(self, name: str, price: int, profit_percentage: float):
        self.name = name
        self.price = price
        self.profit = price * profit_percentage

    def __str__(self):
        return f"name:{self.name} and price:{self.price}"

    @classmethod
    def from_data(cls, filename: str):
        actions = []
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                name = row[0]
                price = row[1]
                profit_percentage = row[2]
                action = cls(name, int(price), float(profit_percentage))
                actions.append(action)

        return actions


class Combination:
    def __init__(self, combination: tuple, total_profit: int):
        self.combi = combination
        self.total_profit = total_profit



