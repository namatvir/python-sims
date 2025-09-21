import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


num_spins = 10000      
bet_amount = 1         
payout = 35            
num_simulations = 100   

numbers = np.arange(37)

def roulette_simulation():
    outcomes = np.zeros(num_spins)
    for i in range(num_spins):
        winning_number = np.random.choice(numbers)
        bet_number = np.random.choice(numbers)  
        if bet_number == winning_number:
            outcomes[i] = bet_amount * payout
        else:
            outcomes[i] = -bet_amount
    return outcomes

results = pd.DataFrame()
for sim in range(num_simulations):
    outcomes = roulette_simulation()
    cumulative_profit = np.cumsum(outcomes)
    results[f'Sim_{sim+1}'] = cumulative_profit

plt.figure(figsize=(12,6))
for col in results.columns:
    plt.plot(results[col], alpha=0.5)
plt.title('Monte Carlo Simulation of Roulette (Single Number Bet)')
plt.xlabel('Number of Spins')
plt.ylabel('Cumulative Profit')
plt.grid(True)
plt.show()

final_profits = results.iloc[-1]
print("Simulation summary:")
print(f"Average final profit/loss: {final_profits.mean():.2f}")
print(f"Maximum profit: {final_profits.max():.2f}")
print(f"Maximum loss: {final_profits.min():.2f}")
