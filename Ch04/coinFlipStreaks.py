#automatetheboringstuff ch4: Coin Flip Sreaks
"""
Write a program to find out how often a streak of six heads or a streak of six
tails comes up in a randomly generated list of heads and tails. Your program
breaks up the experiment into two parts: the first part generates a list of
randomly selected 'heads' and 'tails' values, and the second part checks if
there is a streak in it. Put all of this code in a loop that repeats the
experiment 10,000 times so we can find out what percentage of the coin flips
contains a streak of six heads or tails in a row.
"""

import random


numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails'.
    experiment=[]
    
    for i in range (100):
        experiment.append(random.choice("TH"))
    """
    # A shorter version of the following block:
    for i in range(100):
        if random.randint(0,1):
            experiment.append("T")
        else:
            experiment.append("H")
    """

    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    typeStreak='T'
    currentStreak=0
    
    for i in range(100):
        if(experiment[i]==typeStreak):
            currentStreak+=1
        else:
            currentStreak=1
            typeStreak=experiment[i]

        if currentStreak == 6:
            numberOfStreaks += 1
            currentStreak = 0
            break   # If we find a streak we pass to the next experiment
                    # Without the break, we could also find how many times
                    # a streak come up (e.g. 147% means 1.47 times per experiment

    
print(f'Chance of streak: {numberOfStreaks/100}%')
