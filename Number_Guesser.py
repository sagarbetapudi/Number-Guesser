import random

n = int(input("Enter the range of numbers from 0 to ? : "))

x = random.randrange(0,n)

c = 0
g = 0
while g == 0:
    c=c+1
    k = int(input("Guess?: "))
    if k!=x :
        if k>x:
            print("You have guessed too high")
        else:
            print("You have guessed too low")
    else:
        print("Correct guess... Guessed in "+str(c)+" Times")