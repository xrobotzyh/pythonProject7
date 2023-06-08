from typing import Any, List, Tuple
from model import Combination, Action
import itertools


def find_suitable_actions_combinations(actions: List[Action], max_investment: int) -> List[Combination]:
    suitable_combinations = []
    for i in range(1, len(actions) + 1):
        actions_combinations = itertools.combinations(actions, i)
        for actions_combination in actions_combinations:
            total_cost = 0
            profit = 0
            for action in actions_combination:
                price = action.price
                total_cost = total_cost + price
                # if total_cost
                profit = profit + action.profit
            if total_cost <= max_investment:
                suitable_combinations.append(Combination(actions_combination, round(profit, 2)))
    return suitable_combinations


def find_best_portfolio(actions: List[Action], max_investment: int) -> Combination:
    suitable_combinations = find_suitable_actions_combinations(actions, max_investment)
    suitable_combinations = sorted(suitable_combinations, key=lambda combination: combination.total_profit,
                                   reverse=True)

    return suitable_combinations[0]   


