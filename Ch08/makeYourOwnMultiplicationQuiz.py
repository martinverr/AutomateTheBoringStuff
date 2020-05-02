import time, random

res = 0
correctAnswers=0
while(True):
    for questionNumber in range(10):
        #Asking questions
        t0=time.time()
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        while(True):
            try:
                res=int(input('#%s: %s x %s = ' % (questionNumber+1, num1, num2)))
                if res < 0:
                    print("Retry, your input must be positive")
                    continue
                break
            except ValueError:
                print("Retry, your input must be an integer")

        #Check the result
        if time.time() > t0 + 8:
            print("Time exceeded(8 sec max), next question")
        if res == num1 * num2:
            print("Correct")
            correctAnswers += 1
        else:
            print(f"Wrong, {num1} * {num2} does", num1 * num2)
        time.sleep(1)
    #Showing Stats
    print(f"Score: {correctAnswers}/10")
    print("Want to play again:[yes/no]")
    go=input().lower()
    while(True):
        if go == "yes" or go == "y": break
        elif go == "no" or go == "n": exit()
        else: "Not an answer"
    correctAnswers=0
