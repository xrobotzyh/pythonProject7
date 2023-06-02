import bruteforce
from model import Action

if __name__ == '__main__':
    actions = Action.from_data("actions.csv")
    suitable_actions = bruteforce.find_suitable_actions_combinations(actions, 500)
    max_profit = bruteforce.find_max_profit(suitable_actions)
    bruteforce.display_best_combination(max_profit, suitable_actions)
