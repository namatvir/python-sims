import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


num_spins = 10000
bet_amount = 1
num_simulations = 5

numbers = np.arange(37) 
reds = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
blacks = set(numbers) - reds - {0}

thirds = {1: range(1,13), 2: range(13,25), 3: range(25,37)}

payouts = {
    "single": 35,
    "color": 1,
    "third": 2,
    "multi": None
}

def roulette_simulation(bet_type="single", numbers_to_bet=None):
    outcomes = np.zeros(num_spins)
    for i in range(num_spins):
        winning_number = np.random.choice(numbers)
        
        if bet_type == "single":
            bet_number = numbers_to_bet if numbers_to_bet is not None else np.random.choice(numbers)
            outcomes[i] = bet_amount * payouts["single"] if bet_number == winning_number else -bet_amount

        elif bet_type == "color":
            bet_color = numbers_to_bet if numbers_to_bet is not None else np.random.choice(["red","black"])
            if winning_number == 0:
                outcomes[i] = -bet_amount
            else:
                win_color = "red" if winning_number in reds else "black"
                outcomes[i] = bet_amount * payouts["color"] if bet_color == win_color else -bet_amount

        elif bet_type == "third":
            bet_third = numbers_to_bet if numbers_to_bet is not None else np.random.choice([1,2,3])
            outcomes[i] = bet_amount * payouts["third"] if winning_number in thirds[bet_third] else -bet_amount

        elif bet_type == "multi":

            if numbers_to_bet is None:
                numbers_to_bet = np.random.choice(numbers[1:], size=3, replace=False)
            payout_multi = 36/len(numbers_to_bet) - 1
            outcomes[i] = bet_amount * payout_multi if winning_number in numbers_to_bet else -bet_amount

    return np.cumsum(outcomes)

results = pd.DataFrame()
bet_types = ["single", "color", "third", "multi"]

for bet_type in bet_types:
    for sim in range(num_simulations):
        cum_profit = roulette_simulation(bet_type)
        results[f"{bet_type}_sim{sim+1}"] = cum_profit

plt.figure(figsize=(14,7))
colors_map = {"single":"blue", "color":"red", "third":"green", "multi":"purple"}

plotted = set()

for col in results.columns:
    bet_type = col.split("_")[0]
    if bet_type not in plotted:
        plt.plot(results[col], color=colors_map[bet_type], alpha=0.5, label=bet_type.capitalize())
        plotted.add(bet_type)
    else:
        plt.plot(results[col], color=colors_map[bet_type], alpha=0.5)

plt.title("Monte Carlo Roulette Simulation: Different Bet Types")
plt.legend()
plt.xlabel("Number of Spins")
plt.ylabel("Cumulative Profit")
plt.grid(True)
plt.show()

final_profits = results.iloc[-1]
print(f"Final cumulative profits for each simulation: {final_profits}")