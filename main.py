import bruteforce
import optimized
from model import Stock

if __name__ == '__main__':
    # decimal = 100
    # max_investment = 500
    # filename = "actions.csv"
    # stocks = Stock.from_data(filename, decimal)
    # stocks_brute_force = Stock.from_data(filename, 1)
    # optimized.find_best_portfolio_greedy_algorithm(stocks, max_investment)
    # bruteforce.performance_brute_force(stocks_brute_force, max_investment, filename)

    decimal = 100
    max_investment = 500
    filename = "dataset2.csv"
    stocks = Stock.from_data(filename, decimal)
    optimized.performance_optimized(stocks, max_investment, filename, decimal)

    # decimal = 100
    # max_investment = 500
    # filename = "dataset1.csv"
    # stocks = Stock.from_data(filename, decimal)
    # optimized.performance_optimized_chart(stocks, max_investment, decimal)
