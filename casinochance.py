guesses = input()
g1, g2 = map(int, guesses.split())
values = input()
v1, v2, v3, v4, v5, v6 = map(int, values.split())

def casinoChance():
    count1 = 0
    count2 = 0
    for value in values:
        if (value == g1):
            count1 += 1
        if (value == g2):
            count2 += 1
    chance1 = count1 / 6
    chance2 = count2 / 6
    return chance1 * chance2

print(casinoChance())

