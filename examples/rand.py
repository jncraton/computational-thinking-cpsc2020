import random

if random.random() > .5:
    print("Coin: Heads")
else:
    print("Coin: Tails")

print("Dice roll: ", random.randint(1, 6))

print("Random letter: ", random.choice("abcdefghijklmnopqrstuvwxyz"))
