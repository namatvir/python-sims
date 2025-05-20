#Monte carlo sim for flipping a coin

import random

outcomes = ['heads','tails']

def flip_coin():
    return random.choice(outcomes)

#print (flip_coin())

def MCsim(sample_size: int):
    heads = 0
    tails = 0
    for i in range(sample_size):
        side = flip_coin()
        if side == 'heads':
            heads += 1
        else:
            tails += 1

    return f"The probability of heads is: {100*heads/sample_size}% and the probability of tails is: {100*tails/sample_size}%"

print (MCsim(100000))