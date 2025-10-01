#Purpose: to find the most common roulette number in a list of spins

import random
import numpy as np
import matplotlib.pyplot as plt

num_spins = 10000000

numbers = np.zeros(37) # Initialize counts for numbers 0-36
all_nums = set(range(37))
reds = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
blacks = all_nums - reds - {0}

# Simulate roulette spins
def simulate_spins():
    for i in range(num_spins):
        spin = random.randint(0, 36)
        numbers[spin] += 1
    return numbers

# Find the most common number
def most_common_number(counts):
    max_count = np.max(counts)
    common_numbers = np.where(counts == max_count)[0]
    return common_numbers, max_count

#graph the results
def graph_results(counts):
    plt.bar(range(37), counts, color=['blue' if i in common_numbers
                                      else 'green' if i == 0
                                      else 'red' if i in reds
                                      else 'black' for i in range(37)], width=0.5)
    plt.xlabel('Roulette Number')
    plt.ylabel('Frequency')
    plt.title('Roulette Number Frequency Distribution')
    plt.xticks(range(37), fontsize=9)
    plt.show()

# Main execution
if __name__ == "__main__":
    counts = simulate_spins()
    common_numbers, max_count = most_common_number(counts)
    print(f"The most common number(s): {common_numbers} with {max_count} occurrences.")
    graph_results(counts)

