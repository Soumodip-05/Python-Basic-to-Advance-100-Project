import random
jackpot = random.randint(1,100)

name = input("Please enter your name: ")

guess = int(input("Guess the number between 1 to 100: "))

counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Too low! Guess higher number")
    else:
        print("Too high! Guess lower number")

    guess = int(input("Guess the number between 1 to 100:"))
    counter += 1

print("Awesome job", name, "! 🎉 Huge congratulations on the big win!")
print("You took", counter, "attempts")

