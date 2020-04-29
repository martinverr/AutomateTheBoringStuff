import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)
# 0 is tails, 1 is heads

dictHT = {0:"tails",1:"heads"}  #we need a "translator"

if dictHT[toss] == guess:       #translate toss
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if dictHT[toss] == guess:   #translate toss
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
