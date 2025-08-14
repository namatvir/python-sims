import random
import matplotlib.pyplot as plt

#BASE RULES: 3 reels of 5 symbols each. if 2 of 3 are the same on centre line, return 2x inital bet. If all three are the same, 10x initial bet.
#FUTURE ADDITIONS: Add bonusses for certain symbol outcomes.

def slots():
    
    starting_balance = 5000
    runs = 1000000
    bet_amount = 1
    balance = []
    current_balance = starting_balance

    reel1 = ["🍒", "🍋", "🔔", "7", "BAR", 'test1', 'test2', 'test3', 'test4', 'test5']
    reel2 = ["🍒", "🍋", "🔔", "7", "BAR", 'test1', 'test2', 'test3', 'test4', 'test5']
    reel3 = ["🍒", "🍋", "🔔", "7", "BAR", 'test1', 'test2', 'test3', 'test4', 'test5']

    for _ in range(runs):
        screen1 = random.choice(reel1)
        screen2 = random.choice(reel2)
        screen3 = random.choice(reel3)

        if screen1 == screen2 == screen3:
            current_balance += 10 * bet_amount
        elif screen1 == screen2 or screen1 == screen3 or screen2 == screen3:
            current_balance += 2 * bet_amount
        else:
            current_balance -= bet_amount

        balance.append(current_balance)

    plt.plot(range(1, runs + 1), balance)
    plt.xlabel('Trials')
    plt.ylabel('Balance')
    plt.show()

    if starting_balance > balance[-1]:
        return ('You owe the casino', starting_balance - current_balance)
    elif balance[-1] >= starting_balance:
        return ('Your new balance is', current_balance)

print(slots())

# With only 5 symbols each, results showed clear and consistant profit: Approx $900,000 final balance over 1,000,000 trials
# however when I added an additional 5 symbols (10 total symbols), I consistantly get net negative gains: Approx -$75,000 final balance over 1,000,000 trials
# With 8 total symbols I consistantly gain profit: Approx $150,000 final balance over 1,000,000 trials