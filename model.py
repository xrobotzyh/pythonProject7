import csv
from typing import List, Iterable


class Stock:
    def __init__(self, name: str, price: int, profit_percentage: float, decimal: int):
        self.name = name
        self.price = price
        self.profit_percentage = profit_percentage
        self.profit = price * profit_percentage
        # For the print version
        self.print_price = price / decimal
        self.print_profit = round((self.profit/decimal), 2)

    def __str__(self):
        return f"name:{self.name} and price:{self.print_price} and profit: {self.print_profit}"

    @classmethod
    def from_data(cls, filename: str, decimal):
        actions = []
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                # filter data, ignore negative numbers
                if float(row[1]) > 0:
                    name = row[0]
                    price = row[1]
                    profit_percentage = row[2]
                    # for index of matrix reason,float convert to int
                    action = cls(name, int(float(price) * decimal), float(profit_percentage)/100, decimal)
                    actions.append(action)
                else:
                    continue
        return actions


class Combination:
    def __init__(self, stocks: Iterable[Stock], total_profit: float):
        self.stocks = stocks
        self.total_profit = total_profit

    def __str__(self):
        my_str = f"The max profit of the investment is {self.total_profit}"
        stocks_str = "\n".join([str(stock) for stock in self.stocks])
        return my_str + "\n" + stocks_str
