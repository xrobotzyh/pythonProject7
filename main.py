import time
import psutil

import bruteforce
import optimized
from model import Action

if __name__ == '__main__':
    start_time = time.time()
    memory_before = psutil.virtual_memory().used
    decimal = 1
    actions = Action.from_data("dataset1.csv", decimal)
    max_investment = 500
    # best_combination = bruteforce.find_best_portfolio(actions, max_investment)
    # best_combination = optimized.find_best_portfolio(actions, max_investment)
    best_combination = optimized.find_best_portfolio2(actions, max_investment*decimal)
    end_time = time.time()
    memory_after = psutil.virtual_memory().used
    used_time = end_time - start_time
    memory_used = memory_after - memory_before
    print(best_combination)
    print(f'The time used of the Algorithm is {used_time} seconds ,and memory used is {memory_used / 1000 / 1024}MB')
