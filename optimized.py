from typing import Any, List, Tuple
from model import Combination, Action


def find_best_portfolio_greedy_algorithm(actions: List[Action], max_investment: int):
    # use the best profit first
    best_portfolio = []
    profit = 0
    # sort the actions by their profit_percentage
    actions_sorted_by_profit_percentage = sorted(actions, key=lambda action: action.profit_percentage, reverse=True)
    for action in actions_sorted_by_profit_percentage:
        if max_investment >= action.price:
            best_portfolio.append(action)
            profit = profit + action.profit
            max_investment = max_investment - action.price
    best_combination = Combination(best_portfolio, round(profit, 2))
    return best_combination


def find_best_portfolio_dynamic_programme(actions: List[Action], max_investment: int):
    dp = [[0] * (max_investment + 1) for _ in range(0, len(actions))]
    best_profit = 0
    best_portfolio = []
    # For the first line
    for investment in range(0, (max_investment + 1)):
        if actions[0].price <= investment:
            dp[0][investment] = actions[0].profit
        else:
            dp[0][investment] = 0
    # for the following lines
    for action_index in range(1, len(actions)):
        for investment in range(0, (max_investment + 1)):
            if actions[action_index].price > investment:
                dp[action_index][investment] = dp[action_index - 1][investment]
            else:
                prev_dp_element = dp[action_index-1][investment - actions[action_index].price]
                dp[action_index][investment] = max(dp[action_index - 1][investment], actions[action_index].profit + \
                                                   prev_dp_element)
            best_profit = round(dp[action_index][investment], 2)

    i = len(actions) - 1
    while i > 0 and max_investment > 0:
        if dp[i][max_investment] != dp[i - 1][max_investment]:
            best_portfolio.append(actions[i])
            max_investment = max_investment - actions[i].price
            i = i - 1
        else:
            i = i - 1
    best_portfolio = best_portfolio[::-1]
    best_combination = Combination(best_portfolio, best_profit)
    return best_combination


def find_best_portfolio_dynamic_programme_array(actions: List[Action], max_investment: int):
    profit = [0] * (max_investment + 1)
    best_profit = 0
    best_portfolio = []
    # initializer the list use the first line
    for investment in range(0, (max_investment+1)):
        if actions[0].price <= investment:
            profit[investment] = actions[0].profit
    # for the following lines,use a dynamic array next_line_profit
    next_line_profit = profit.copy()
    for action_index in range(1, len(actions)):
        for investment in range(0, (max_investment + 1)):
            if actions[action_index].price <= investment:
                next_line_profit[investment] = max(profit[investment], actions[action_index].profit + \
                                                   profit[investment - actions[action_index].price])
        profit = next_line_profit.copy()
    best_profit = round(profit[max_investment], 2)

    # i = len(actions) - 1
    # while i > 0 and max_investment > 0:
    #     if dp[i][max_investment] != dp[i - 1][max_investment]:
    #         best_portfolio.append(actions[i])
    #         max_investment = max_investment - actions[i].price
    #         i = i - 1
    #     else:
    #         i = i - 1
    # best_portfolio = best_portfolio[::-1]
    # best_combination = Combination(best_portfolio, best_profit)
    return best_profit

