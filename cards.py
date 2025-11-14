import random

Iterations = 10000000
Spades = 0
Hearts = 0
Diamonds = 0
Clubs = 0

for i in range(Iterations):
    cards = ["Ace_Hearts", "2_Hearts", "3_Hearts", "4_Hearts", "5_Hearts",
         "6_Hearts", "7_Hearts", "8_Hearts", "9_Hearts", "10_Hearts",
         "Jack_Hearts", "Queen_Hearts", "King_Hearts",
         "Ace_Diamonds", "2_Diamonds", "3_Diamonds", "4_Diamonds", "5_Diamonds",
         "6_Diamonds", "7_Diamonds", "8_Diamonds", "9_Diamonds", "10_Diamonds",
         "Jack_Diamonds", "Queen_Diamonds", "King_Diamonds",
         "Ace_Clubs", "2_Clubs", "3_Clubs", "4_Clubs", "5_Clubs",
         "6_Clubs", "7_Clubs", "8_Clubs", "9_Clubs", "10_Clubs",
         "Jack_Clubs", "Queen_Clubs", "King_Clubs",
         "Ace_Spades", "2_Spades", "3_Spades", "4_Spades", "5_Spades",
         "6_Spades", "7_Spades", "8_Spades", "9_Spades", "10_Spades",
         "Jack_Spades", "Queen_Spades", "King_Spades"]
    random.shuffle(cards)
    drawn_card = cards[random.randint(0, 51)]
    if "Spades" in drawn_card:
        Spades += 1
    elif "Hearts" in drawn_card:
        Hearts += 1
    elif "Diamonds" in drawn_card:
        Diamonds += 1
    elif "Clubs" in drawn_card:
        Clubs += 1

print("Spades:", Spades)
print("Hearts:", Hearts)
print("Diamonds:", Diamonds)
print("Clubs:", Clubs)
print("Total Cards Drawn:", Iterations)
print("Percentage Spades:", (Spades / Iterations) * 100, "%")
print("Percentage Hearts:", (Hearts / Iterations) * 100, "%")
print("Percentage Diamonds:", (Diamonds / Iterations) * 100, "%")
print("Percentage Clubs:", (Clubs / Iterations) * 100, "%")