from statistics import NormalDist
import random
import math

i = []
while True:
    guess = input("Guess a number (or 'q' to quit): ")
    if guess == "q":
        break
    if guess == '':
        continue
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    i.append(guess)

sum_of_guesses = sum(int(x) for x in i)
mean = sum_of_guesses / len(i)
std_dev = math.sqrt(sum((int(x) - mean) ** 2 for x in i) / len(i))
print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")
dist = NormalDist(mu=mean, sigma=std_dev)

print(i)