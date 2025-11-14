import random

sportscar = 0
goat = 0
repeats = 0

while repeats < 100000000:

    doors = ['goat', 'goat', 'sportscar']
    random.shuffle(doors)

    selection = random.randint(0, 2)

    if doors[selection] == 'sportscar':
        goat += 1
    else:
        sportscar += 1
    repeats += 1

print("Sports Car:",sportscar)
print("Goat:",goat)
print("Total:",repeats)
print("Winning Percentage:",(sportscar/repeats)*100,"%")
