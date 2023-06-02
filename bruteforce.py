from typing import Any, List
from model import Action, Combination
import itertools


def find_suitable_actions_combinations(source: Any, max_investment: int) -> List[Combination]:
    suitable_actions = []
    for i in range(1, len(source) + 1):
        actions_combinations = itertools.combinations(source, i)
        for action in actions_combinations:
            total_cost = 0
            i = 0
            profit = 0
            while i < len(action):
                price = action[i].price
                total_cost = total_cost + price
                profit = profit + action[i].profit
                i += 1
            if total_cost < max_investment:
                suitable_actions.append(Combination(action, round(profit, 2)))
    return suitable_actions


def find_max_profit(suitable_actions: List[Combination]) -> float:
    all_profits = []
    for action in suitable_actions:
        all_profits.append(action.total_profit)
    max_profit = max(all_profits)
    return max_profit


def display_best_combination(max_profit: float, suitable_actions: List[Combination]):
    print(f'The max profit of the investment is {max_profit}')
    for suitable_action in suitable_actions:
        if suitable_action.total_profit == max_profit:
            for action in suitable_action.combi:
                print(action)



