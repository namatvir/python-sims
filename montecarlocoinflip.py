import random
import matplotlib.pyplot as plt

def coinflip():
    return random.choice(['heads','tails'])

def mccf(runs):

    heads = 0
    tails = 0
    numberofheads = []

    for i in range(runs):
        if coinflip() == 'heads':
            heads += 1
        else:
            tails += 1
        numberofheads.append(heads)

    print (
        'Over ', runs, 'runs, the percentage of heads is:', (heads/runs)*100,'% ,and tails is:',(tails/runs)*100,'%.'
        #f"Over {runs} runs, the percentage of heads is: {(heads/runs)*100:.2f}%, "
        #f"and tails is: {(tails/runs)*100:.2f}%"
        )
    return numberofheads


runs = int(input("How many trials would you like to run?:"))
numberofheads = mccf(runs)

plt.plot(range(1, runs + 1), numberofheads)
plt.xlabel('heads over time')
plt.ylabel('# of runs')
plt.show()