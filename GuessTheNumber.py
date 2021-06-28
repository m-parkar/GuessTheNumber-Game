import random
import math
number=random.randint(1,100)
print("\n\tYou've only ",round(math.log(100 - 1 + 1, 2))," chances to guess the integer!\n")
Turns = 0

while Turns < math.log(100 - 1 + 1, 2):
    Turns += 1

    guess=int(input("Guess the Number :"))

    if guess == number:
        print("Your guess is absolutely correct. Thankyou for playing with us !")
        break
    elif guess < number:
        print("You need to Guess Higher. Try again")

    elif guess > number:
        print("You need to Guess Lower. Try again")
        
if Turns >= math.log(100 - 1 + 1, 2):
    print("\nThe number is: ", number)
    print("\tBetter Luck Next time!")
