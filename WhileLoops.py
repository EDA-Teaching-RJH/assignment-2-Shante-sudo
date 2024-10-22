import random
guess = int(input("guess a the number from 1 to 10"))
num = random.randint(1, 10)
while guess != num:
    guess = int(input("inncorect, guess again"))
else:
    print("Correct, the number is " + str(num))
