from typing import Any, List, Tuple
from model import Combination, Action


def find_best_portfolio(actions: List[Action], max_investment: int):
    # Greedy Algorithm*
    best_portfolio = []
    profit = 0
    actions_sorted_by_profit_percentage = sorted(actions, key=lambda action: action.profit_percentage, reverse=True)
    for action in actions_sorted_by_profit_percentage:
        if max_investment >= action.price:
            best_portfolio.append(action)
            profit = profit + action.profit
            max_investment = max_investment - action.price
            if max_investment < actions_sorted_by_profit_percentage[-1].price:
                break
    best_combination = Combination(best_portfolio, round(profit, 2))
    return best_combination


def find_best_portfolio2(actions: List[Action], max_investment: int):
    dp = [[0] * (max_investment + 1) for _ in range(0, len(actions))]
    best_profit = 0
    best_portfolio = []
    for action_index in range(0, len(actions)):
        for investment in range(0, (max_investment + 1)):
            if actions[action_index].price > investment:
                dp[action_index][investment] = dp[action_index - 1][investment]
            else:
                dp[action_index][investment] = max(dp[action_index - 1][investment], actions[action_index].profit + \
                                                   dp[action_index - 1][investment - actions[action_index].price])
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


def find_best_portfolio_float(actions: List[Action], max_investment: int, decimal: int):
    for action in actions:
        action.price = action.price * decimal
    max_investment = max_investment * decimal
    return actions, max_investment
