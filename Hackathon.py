import random
import time
import sys

def clear_lines(n):
    for _ in range(n):
        sys.stdout.write("\033[F\033[K")

# ============================
#   NEW VIRTUAL REALM ONLINE
# ============================
def virtual_realm_online():

    print("VIRTUAL REALM ONLINE")
    print('type "LINK START" to begin.')

    # intro
    while True:
        command = input("> ")
        if command == "LINK START":
            print("\nConnection established...")
            time.sleep(.5)
            print("Initializing neural interface.")
            time.sleep(.5)
            print("Synchronizing avatar data.")
            time.sleep(1.5)
            print("\nWELCOME TO THE FLOATING CASTLE, AINCRAD.")
            print("if your HP reaches zero, your life ENDS.")
            print("\nClear the castle to escape.")
            time.sleep(3)

            for _ in range(11):
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
            break
        else:
            print('Connection terminated, try again.')

    # player stats
    player = {"hp": 100, "atk_min": 8, "atk_max": 15, "gold": 0, "inventory": []}

    # room descriptions
    rooms = {
        "atrium": {
            "name": "Atrium of First Light",
            "desc": "A vast chamber with floating lanterns and marble pillars.",
            "enemy": {"name": "Lantern Wisp", "desc": "A flickering spirit of light.", "hp": 25, "atk_min": 4, "atk_max": 7, "alive": True, "gold_reward": 10},
            "connections": {"north": "library", "east": "hall"},
            "is_shop": False
        },
        "library": {
            "name": "Clockwork Library",
            "desc": "Shelves twist like gears; timepieces tick in unison.",
            "enemy": {"name": "Cogbound Scholar", "desc": "A stitched automaton clutching a brass tome.", "hp": 35, "atk_min": 6, "atk_max": 10, "alive": True, "gold_reward": 15},
            "connections": {"south": "atrium", "west": "garden"},
            "is_shop": False
        },
        "hall": {
            "name": "Echoing Hall",
            "desc": "Every whisper becomes a chorus; shadows move oddly.",
            "enemy": {"name": "Hollow Echo", "desc": "A shadow that mimics your strikes.", "hp": 30, "atk_min": 5, "atk_max": 9, "alive": True, "gold_reward": 12},
            "connections": {"west": "atrium", "north": "throne"},
            "is_shop": False
        },
        "garden": {
            "name": "Garden of Mirrors",
            "desc": "Paths split between reflections; the sky shimmers below.",
            "enemy": {"name": "Reflected Knight", "desc": "A shimmering warrior born of glass.", "hp": 40, "atk_min": 7, "atk_max": 12, "alive": True, "gold_reward": 18},
            "connections": {"east": "library", "north": "shop"},
            "is_shop": False
        },
        "throne": {
            "name": "Throne of Clouds",
            "desc": "A throne suspended on a cloud platform, wind singing around it.",
            "enemy": {"name": "Sky Sovereign", "desc": "A regal figure wreathed in storms.", "hp": 60, "atk_min": 9, "atk_max": 16, "alive": True, "gold_reward": 25},
            "connections": {"south": "hall"},
            "is_shop": False
        },
        "shop": {
            "name": "Merchant's Shop",
            "desc": "A merchant's stall with potions and upgrades.",
            "enemy": None,
            "connections": {"south": "garden"},
            "is_shop": True
        }
    }

    current_room = "atrium"

    # Combat function
    def start_combat(room):
        enemy = room["enemy"]
        if not enemy or not enemy.get("alive", True):
            return True

        print(f"\nAn enemy appears: {enemy['name']} - {enemy['desc']}")
        print(f"Enemy HP: {enemy['hp']}")

        while enemy["hp"] > 0 and player["hp"] > 0:
            action = input("(Combat) Type ATTACK to strike: ")
            if action == "ATTACK":
                dmg = random.randint(player["atk_min"], player["atk_max"])
                enemy["hp"] -= dmg
                print(f"You hit {enemy['name']} for {dmg} damage.")

                if enemy["hp"] <= 0:
                    enemy["alive"] = False
                    player["gold"] += enemy["gold_reward"]
                    print(f"{enemy['name']} defeated! +{enemy['gold_reward']} gold. Total: {player['gold']}")
                    return True

                edmg = random.randint(enemy["atk_min"], enemy["atk_max"])
                player["hp"] -= edmg
                print(f"{enemy['name']} hits you for {edmg}. HP: {player['hp']}")

                if player["hp"] <= 0:
                    print("Your HP reached zero. You have died. GAME OVER.")
                    return False

            elif action == "LOOK":
                print(room["desc"])
                print(f"Enemy HP: {enemy['hp']}")
            else:
                print("Unknown combat command.")
                time.sleep(2)
                for _ in range(2):
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[K")

        return True

    # Shop function
    def shop():
        print("\nWelcome to the shop!")
        print("1. Health Potion - 10 gold (restores 20 HP)")
        print("2. Attack Upgrade - 20 gold (+2 attack)")
        choice = input("Choose or type BACK: ")

        if choice == "1":
            if player["gold"] >= 10:
                player["gold"] -= 10
                player["inventory"].append("Health Potion")
                print("Bought Health Potion!")
            else:
                print("Not enough gold.")
        elif choice == "2":
            if player["gold"] >= 20:
                player["gold"] -= 20
                player["atk_min"] += 2
                player["atk_max"] += 2
                print("Attack upgraded!")
            else:
                print("Not enough gold.")
        elif choice == "BACK":
            return
        else:
            print("Invalid choice.")

    # Show directions
    def print_directions():
        print("Available directions:")
        for d in rooms[current_room]["connections"]:
            print(f"{d.upper()}: {rooms[rooms[current_room]['connections'][d]]['name']}")

    # Start game
    print(f"\nYou are in: {rooms[current_room]['name']}")
    print(rooms[current_room]['desc'])
    print("\nCommands: NORTH, SOUTH, EAST, WEST, LOOK, INVENTORY, USE, QUIT")
    print_directions()

    # Main loop
    while True:
        cmd = input("> ")

        if cmd in ["NORTH", "SOUTH", "EAST", "WEST"]:
            direction = cmd.lower()
            if direction in rooms[current_room]["connections"]:
                current_room = rooms[current_room]["connections"][direction]
                print(f"\nYou move to: {rooms[current_room]['name']}")
                print(rooms[current_room]['desc'])

                if rooms[current_room]["is_shop"]:
                    shop()
                else:
                    alive = start_combat(rooms[current_room])
                    if not alive:
                        break

                print_directions()
            else:
                print("You can't go that way.")

        elif cmd == "LOOK":
            print(rooms[current_room]["desc"])
            enemy = rooms[current_room]["enemy"]
            if enemy and enemy.get("alive", True):
                print(f"Enemy: {enemy['name']} (HP: {enemy['hp']})")
            else:
                print("No enemies here.")

        elif cmd == "INVENTORY":
            if player["inventory"]:
                print("Inventory:")
                for i, item in enumerate(player["inventory"], 1):
                    print(f"{i}. {item}")
            else:
                print("Inventory empty.")

        elif cmd == "USE":
            if not player["inventory"]:
                print("No items to use.")
                continue

            print("Inventory:")
            for i, item in enumerate(player["inventory"], 1):
                print(f"{i}. {item}")

            choice = input("Choose item number: ")
            try:
                idx = int(choice) - 1
                item = player["inventory"][idx]

                if item == "Health Potion":
                    player["hp"] = min(100, player["hp"] + 20)
                    player["inventory"].pop(idx)
                    print(f"Used Health Potion. HP: {player['hp']}")
                else:
                    print("Can't use that.")
            except:
                print("Invalid choice.")

        elif cmd == "QUIT":
            print("Exiting the interface. Connection closed.")
            break

        else:
            print("Unknown command.")

# ============================
#   SECOND GAME PLACEHOLDER
# ============================
def game_two():
    import random
    import time

    # Create deck
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King", "Ace")
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    deck_list = deck.copy()

    # Card value function
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

    print("\n=== CARD DUEL ===")
    print("Pick a card from your hand\n")

    # Player hand
    player_hand = random.sample(deck_list, 5)
    for card in player_hand:
        deck_list.remove(card)

    print("Your hands cards:")
    for i, card in enumerate(player_hand, 1):
        print(f"{i}. {card}")

    # Player chooses card
    while True:
        try:
            print()
            choice = int(input("Choose a card number (1-5): "))
            if 1 <= choice <= 5:
                user_card = player_hand[choice - 1]
                break
        except:
            pass
        print("Choose only 1 - 5")

    print()
    print(f"You chose: {user_card}")

    # Computer hand + choice
    computer_hand = random.sample(deck_list, 5)
    for card in computer_hand:
        deck_list.remove(card)

    computer_card = random.choice(computer_hand)
    print()
    print(f"Computer chose: {computer_card}")

    # Determine winner
    print()
    time.sleep(1)

    if card_value(user_card) > card_value(computer_card):
        print("You win")
    elif card_value(user_card) < card_value(computer_card):
        print("The Computer has won")
    else:
        print("Its a tie")

    print("\nPress Enter to return to the main hub")
    input()
    for _ in range(21):
                        sys.stdout.write("\033[F")
                        sys.stdout.write("\033[K")


# ============================
#         MAIN MENU
# ============================
while True:
    print("============================")
    print("     HACKATHON GAME HUB     ")
    print("============================")
    print(" 1. Virtual Realm Online    ")
    print(" 2. Card Duel               ")
    print(" Q. Exit                    ")
    print("============================")

    choice = input(" Choose your path: ").strip().lower()
    clear_lines(8)

    if choice == '1':
        virtual_realm_online()
    elif choice == '2':
        game_two()
    elif choice == '3':
        print("Closing")
        break
    else:
        print("Choose 1 - 3 only")  
