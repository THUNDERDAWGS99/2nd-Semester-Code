import random
import time

class Dice:
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        return random.randint(1, self.sides)

class D4(Dice):
    def __init__(self):
        super().__init__(4)

class D6(Dice):
    def __init__(self):
        super().__init__(6)

class D8(Dice):
    def __init__(self):
        super().__init__(8)

class D10(Dice):
    def __init__(self):
        super().__init__(10)

class D12(Dice):
    def __init__(self):
        super().__init__(12)

class D20(Dice):
    def __init__(self):
        super().__init__(20)

class D100(Dice):
    def __init__(self):
        super().__init__(100)

if __name__ == "__main__":
    dice = [D4(), D6(), D8(), D10(), D12(), D20(), D100()]

    print("Press Enter to roll dice")
    input()

    print("Rolling dice...")
    time.sleep(1)
    for die in dice:
        print(f"D{die.sides}: {die.roll()}")
