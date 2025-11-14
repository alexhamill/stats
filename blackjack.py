import random

deck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]*4

dealer = 0
player = 0
Iterations = 1000000

for i in range(Iterations):
    playdeck = deck.copy()
    random.shuffle(playdeck)
    player_hand = [playdeck.pop(), playdeck.pop()]
    dealer_hand = [playdeck.pop(), playdeck.pop()]


    while sum(player_hand) < 17:
        player_hand.append(playdeck.pop())
        if sum(player_hand) > 21 and 11 in player_hand:
            player_hand[player_hand.index(11)] = 1
        if sum(player_hand) > 21:
            dealer += 1
            break

    while sum(dealer_hand) < 17:
        dealer_hand.append(playdeck.pop())
        if sum(dealer_hand) > 21 and 11 in dealer_hand:
            dealer_hand[dealer_hand.index(11)] = 1
        if sum(dealer_hand) > 21:
            player += 1
            break

    if sum(player_hand) > sum(dealer_hand) and sum(player_hand) <= 21:
        player += 1
    elif sum(dealer_hand) > sum(player_hand) and sum(dealer_hand) <= 21:
        dealer += 1 

print("Player Wins:",player)
print("Dealer Wins:",dealer)
print("Total Games:",Iterations)
print("Player Winning Percentage:",(player/Iterations)*100,"%")
print("Dealer Winning Percentage:",(dealer/Iterations)*100,"%")
    
