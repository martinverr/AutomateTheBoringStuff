#automatetheboringstuff ch4: Coin Flip Sreaks

import random


numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails'.
    experiment=[]
    
    for i in range (100):
        experiment.append(random.choice("TH"))
    """
    #instead of
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
            typeStreak==experiment[i]

        if currentStreak == 6:
            numberOfStreaks += 1
            currentStreak = 0
            break   #If we find a streak we pass to the next experiment

    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
