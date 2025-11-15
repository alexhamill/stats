import random

Iterations = 10000000
doors = 1000
removes = 99

n = doors
if removes > n - 2:
    raise ValueError("removes must be <= number of other doors - 1")

sportscar = 0
goat = 0

for _ in range(Iterations):
    car = random.randrange(n)     
    sel = random.randrange(n)     
    
    if car != sel:
        if random.randrange(n - removes - 1) == 0:
            sportscar += 1
        else:
            goat += 1
    else:
        goat += 1

# goat = Iterations - sportscar

print("Sports Car:", sportscar)
print("Goat:", goat)
print("Total:", Iterations)
print("Winning Percentage:", (sportscar / Iterations) * 100, "%")
