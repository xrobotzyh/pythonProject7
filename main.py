import bruteforce
import optimized
from model import Stock


if __name__ == '__main__':
    decimal = 100
    max_investment = 500
    filename = "dataset1.csv"
    stocks = Stock.from_data(filename, decimal)
    stocks_brute_force = Stock.from_data(filename, 1)
    bruteforce.performance_brute_force(stocks_brute_force[:21], max_investment, filename)
    optimized.performance_optimized(stocks[:21], max_investment, filename, decimal)
