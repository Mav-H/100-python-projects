import random

rand_num = random.randrange(0, 100, 1)

print(rand_num)

while True:
    guess = input("Guess the random number: ")

    if int(guess) == rand_num:
        print("You win!")
        break
    else:
        if int(guess) > rand_num:
            print("Too high!")
        else: 
            print("Too low!")
   
