import random

#creates tuple of multiple cards
suits = ("Hearts", "Diamonds", "Clubs", "Spades")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10",
         "Jack", "Queen", "King", "Ace")

deck = tuple(f"{rank} of {suit}" for suit in suits for rank in ranks)

#turn the tuple into a a list so cards can be removed
deck_list = list(deck)

#function to get value of card so they can be compared
def card_value(card):
    rank = card.split()[0]
    order = {
        "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,
        "Jack":11, "Queen":12, "King":13, "Ace":14
    }
    return order[rank]

#gives the user a random card
user_card = random.choice(deck_list)
deck_list.remove(user_card)
print(f"You drew: {user_card}")

cardswaps = 3
while cardswaps > 0:
    choice = input("Do you want to redraw your card (yes/no): ").lower()
    if choice == "yes":
        new_card = random.choice(deck_list)
        deck_list.remove(new_card)
        print(f"Your new card is: {new_card}")
        user_card = new_card
        cardswaps -= 1
    else:
        break

print(f"Your card is: {user_card}")

#computers card
computer_card = random.choice(deck_list)
print(f"Computer drew: {computer_card}")

#determings the winner based on value of the cards
if card_value(user_card) > card_value(computer_card):
    print("You win")
elif card_value(user_card) < card_value(computer_card):
    print("Computer wins")
else:
    print("Tie")
