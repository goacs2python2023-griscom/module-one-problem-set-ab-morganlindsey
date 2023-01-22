import random
def sumDice():
    roll1 = random.randInt(1,6)
    roll2 = random.randInt(1,6)
    sum = roll1 + roll2
    if (sum == 6 or sum == 7 or sum == 8):
        return ("Win")
    else:
        return ("Lose")
print(sumDice())
