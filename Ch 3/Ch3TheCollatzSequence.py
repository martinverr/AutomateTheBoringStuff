#Automatetheboringstuff ch3, practice: The collatz Sequence

def collatz(number):
    # exceptional case
    if number == 0:
        print("1")
        return
    
    # if base case
    if number == 1:
        return
    
    # if number is odd
    if number % 2:
        print(3*number+1)
        return collatz(3*number+1)

    # if number is even
    print(number//2)
    return collatz(number//2)

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

inputInt = collatz(inputInt)
