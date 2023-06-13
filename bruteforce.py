import time
from typing import List
import psutil
import rapport
from model import Combination, Stock
import itertools


def find_suitable_stocks_combinations(stocks: List[Stock], max_investment: int) -> List[Combination]:
    suitable_combinations = []
    for i in range(1, len(stocks) + 1):
        stocks_combinations = itertools.combinations(stocks, i)
        for stocks_combination in stocks_combinations:
            total_cost = 0
            profit = 0
            for stock in stocks_combination:
                price = stock.price
                total_cost = total_cost + price
                profit = profit + stock.profit
            if total_cost <= max_investment:
                suitable_combinations.append(Combination(stocks_combination, round(profit, 2)))
    return suitable_combinations


def find_best_portfolio(stocks: List[Stock], max_investment: int):
    suitable_combinations = find_suitable_stocks_combinations(stocks, max_investment)
    suitable_combinations = sorted(suitable_combinations, key=lambda combination: combination.total_profit,
                                   reverse=True)
    total_investment = 0
    number_stocks = 0
    for stock in suitable_combinations[0].stocks:
        total_investment += stock.price
        number_stocks += 1
    return suitable_combinations[0], total_investment, number_stocks


def performance_brute_force(stocks, max_investment, filename):
    start_time = time.time()
    memory_before = psutil.virtual_memory().used
    best_combination, total_investment, number_stocks = find_best_portfolio(stocks, max_investment)
    end_time = time.time()
    memory_after = psutil.virtual_memory().used
    used_time = end_time - start_time
    memory_used = (memory_after - memory_before) / 1000 / 1024
    report_title, columns, report_data = rapport.report(best_combination, filename + "bf")
    rapport.generate_report(report_title, columns, report_data, best_combination.total_profit, used_time,
                            memory_used,
                            total_investment, number_stocks)
    print(best_combination)
    print(f'The time used of the Algorithm brut force is {used_time} seconds ,and memory used is {memory_used}MB \n')
