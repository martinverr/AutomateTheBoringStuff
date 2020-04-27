#Automatetheboringstuff ch3, practice: The collatz Sequence

def collatz(number):
    if number == 1:
        print("1")
        return 1
    if not number % 2:    #if number is even
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1

#_______________MAIN_____________________

while(True):
    try:
        inputInt = int(input("Integer: "))
        if inputInt>0:
            break
        else:
            print("Must be positive")
    except(ValueError):
        print("Type an integer")



#DO WHILE (instead of an infinite loop with break)
inputInt = collatz(inputInt)
while inputInt!=1:
    inputInt=collatz(inputInt)
