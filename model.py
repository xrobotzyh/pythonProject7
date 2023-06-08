import csv
from typing import List, Iterable


class Action:
    def __init__(self, name: str, price: int, profit_percentage: float):
        self.name = name
        self.price = price
        self.profit_percentage = profit_percentage / 100
        self.profit = price * profit_percentage / 100

    def __str__(self):
        return f"name:{self.name} and price:{self.price} and profit: {self.profit}"

    @classmethod
    def from_data(cls, filename: str, decimal):
        actions = []
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                name = row[0]
                price = int(float(row[1])*decimal)
                profit_percentage = row[2]
                action = cls(name, int(price), float(profit_percentage))
                actions.append(action)

        return actions


class Combination:
    def __init__(self, actions: Iterable[Action], total_profit: float):
        self.actions = actions
        self.total_profit = total_profit

    def __str__(self):
        my_str = f"The max profit of the investment is {self.total_profit}"
        actions_str = "\n".join([str(action) for action in self.actions])
        return my_str + "\n" + actions_str
