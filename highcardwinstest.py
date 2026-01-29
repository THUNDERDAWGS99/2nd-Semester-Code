import random
import time

#creates tuple and deck of the multiple cards
suits = ("Hearts", "Diamonds", "Clubs", "Spades")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King", "Ace")
deck = tuple(f"{rank} of {suit}" for suit in suits for rank in ranks)
deck_list = list(deck)

#function to get value of card so they can be compared
def card_value(card):
    rank = card.split()[0]
    suit = card.split()[-1]
    order = {
        "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,
        "Jack":11, "Queen":12, "King":13, "Ace":14
    }
    suit_order = {
        "Clubs":1,
        "Diamonds":2,
        "Hearts":3,
        "Spades":4
    }
    return (order[rank], suit_order[suit]) 

#player gets their 5 cards
player_hand = random.sample(deck_list, 5)
for card in player_hand:
    deck_list.remove(card)
print("Your hand:")
for i, card in enumerate(player_hand, 1):
    print(f"{i}. {card}")

# player chooses 1 card from their hand
while True:
    try:
        print(" ")
        choice = int(input("Choose a card number (1-5): "))
        if 1 <= choice <= 5:
            user_card = player_hand[choice - 1]
            break
    except:
        pass
    print("CHOOSE ONLY FROM 1-5!")

print(" ")
print(f"You choosed: {user_card}")

#computer chooses from its 5 cards
computer_hand = random.sample(deck_list, 5)
for card in computer_hand:
    deck_list.remove(card)
computer_card = random.choice(computer_hand)
print(" ")
print(f"Computer choosed: {computer_card}")

#determins winner
if card_value(user_card) > card_value(computer_card):
    time.sleep(1)
    print(" ")
    print("You win :D")
elif card_value(user_card) < card_value(computer_card):
    time.sleep(1)
    print(" ")
    print("Computer wins >:(")
else:
    time.sleep(1)
    print(" ")
    print("Tie :(")
