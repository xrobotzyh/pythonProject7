import time
import psutil

import bruteforce
import optimized
import rapport
from model import Action
from rapport import report,display_report_template

if __name__ == '__main__':
    start_time = time.time()
    memory_before = psutil.virtual_memory().used
    decimal = 1
    actions = Action.from_data("actions.csv", decimal)
    max_investment = 500
    # best_combination = bruteforce.find_best_portfolio(actions, max_investment)
    # best_combination = optimized.find_best_portfolio_greedy_algorithm(actions, max_investment*decimal)
    best_combination = optimized.find_best_portfolio_dynamic_programme(actions, max_investment, decimal)
    # best_combination = optimized.find_best_portfolio_dynamic_programme_array(actions, max_investment * decimal)

    end_time = time.time()
    memory_after = psutil.virtual_memory().used
    used_time = end_time - start_time
    memory_used = memory_after - memory_before
    report_title, columns, report_data = rapport.report(best_combination,"action")
    rapport.generate_report(report_title, columns, report_data,best_combination.total_profit,used_time,memory_used)
    print(best_combination)
    print(f'The time used of the Algorithm is {used_time} seconds ,and memory used is {memory_used / 1000 / 1024}MB')
