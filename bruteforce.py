import time
from typing import List
import psutil
import rapport
from model import Combination, Stock
import itertools
import matplotlib.pyplot as chart


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
    best_combination, total_investment, number_stocks = find_best_portfolio(stocks, max_investment)
    end_time = time.time()
    used_time = end_time - start_time
    memory_used = psutil.Process()
    memory_usage = memory_used.memory_info().rss / 1024 / 1024
    report_title, columns, report_data = rapport.report(best_combination, filename + "bf")
    rapport.generate_report(report_title, columns, report_data, best_combination.total_profit, used_time,
                            memory_usage,
                            total_investment, number_stocks)
    print(best_combination)
    print(f'The time used of the Algorithm brut force is {used_time} seconds ,and memory used is {memory_usage}MB \n')


def performance_brute_force_chart(stocks, max_investment):
    execution_times = []
    num_stocks = []
    memory_usages = []

    for i in range(1, len(stocks) + 1):
        stock = stocks[:i]
        start_time = time.time()
        find_best_portfolio(stock, max_investment)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
        process = psutil.Process()
        memory_usage = process.memory_info().rss / 1024 / 1024
        memory_usages.append(memory_usage)
        num_stocks.append(i)

    chart.plot(num_stocks, execution_times)
    chart.title('Brut Force Algorithm Performance')
    chart.xlabel('Number of Stocks')
    chart.ylabel('Execution Time')
    chart.show()

    chart.plot(num_stocks, memory_usages)
    chart.title('Algorithm Performance')
    chart.xlabel('Number of Stocks')
    chart.ylabel('Memory Usage (MB)')
    chart.show()
