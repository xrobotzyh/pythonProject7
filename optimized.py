import time
from typing import List
import psutil
import rapport
from model import Combination, Stock


def find_best_portfolio_greedy_algorithm(stocks: List[Stock], max_investment: int):
    # use the best profit first
    decimal = 1
    best_portfolio = []
    profit = 0
    # sort the actions by their profit_percentage
    stocks_sorted_by_profit_percentage = sorted(stocks, key=lambda action: action.profit_percentage, reverse=True)
    for stock in stocks_sorted_by_profit_percentage:
        if max_investment >= stock.price:
            best_portfolio.append(stock)
            profit = profit + stock.profit
            max_investment = max_investment - stock.price
    best_combination = Combination(best_portfolio, round(profit, 2))
    return best_combination


def find_best_portfolio_dynamic_programme(stocks: List[Stock], max_investment: int, decimal: int):
    max_investment = max_investment * decimal
    dp = [[0] * (max_investment + 1) for _ in range(0, len(stocks))]

    best_portfolio = []
    # For the first line,if the price of the action < max investment, use the element,else fill the table by 0
    for investment in range(0, (max_investment + 1)):
        if stocks[0].price <= investment:
            dp[0][investment] = stocks[0].profit
        else:
            dp[0][investment] = 0
    # for the following lines
    for stock_index in range(1, len(stocks)):
        for investment in range(0, (max_investment + 1)):
            # If the profit of last line at the same row is not egal, it means the element has been used
            if stocks[stock_index].price > investment:
                dp[stock_index][investment] = dp[stock_index - 1][investment]
            else:
                prev_dp_element = dp[stock_index - 1][investment - stocks[stock_index].price]
                dp[stock_index][investment] = max(dp[stock_index - 1][investment], stocks[stock_index].profit + \
                                                  prev_dp_element)
    best_profit = round(dp[len(stocks) - 1][max_investment] / decimal, 2)

    i = len(stocks) - 1
    number_actions = 0
    total_investment = 0
    while i >= 0 and max_investment > 0:
        # If the profit of last line same row is not egal, it means the element has been used
        if dp[i][max_investment] == dp[i - 1][max_investment - stocks[i].price] + stocks[i].profit:
            best_portfolio.append(stocks[i])
            max_investment = max_investment - stocks[i].price
            total_investment = total_investment + stocks[i].price
            i = i - 1
            number_actions += 1
        else:
            i = i - 1
    total_investment = total_investment / decimal
    best_portfolio = best_portfolio[::-1]
    best_combination = Combination(best_portfolio, best_profit)
    return best_combination, total_investment, number_actions


def performance_optimized(stocks, max_investment, filename, decimal):
    start_time = time.time()
    memory_before = psutil.virtual_memory().used
    best_combination, total_investment, number_stocks = find_best_portfolio_dynamic_programme(stocks, max_investment,
                                                                                              decimal)
    end_time = time.time()
    memory_after = psutil.virtual_memory().used
    used_time = end_time - start_time
    memory_used = (memory_after - memory_before) / 1000 / 1024
    report_title, columns, report_data = rapport.report(best_combination, filename + "opz")
    rapport.generate_report(report_title, columns, report_data, best_combination.total_profit, used_time,
                            memory_used,
                            total_investment, number_stocks)
    print(best_combination)
    print(f'The time used of the Algorithm optimized is {used_time} seconds ,and memory used is {memory_used}MB')
