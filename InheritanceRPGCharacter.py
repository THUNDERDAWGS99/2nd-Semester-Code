#main class
class RPGCharacter:
    def __init__(self, name, health, attack_power, level):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.level = level

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage")
        target.take_damage(self.attack_power)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage, Health is now {self.health}.")

    def display_stats(self):
        print(f"--- {self.name}'s Stats ---")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Level: {self.level}")
        print("--------------------------")


                                                #Sub classes

#warrior
class Warrior(RPGCharacter):
    def __init__(self, name, health, attack_power, level):
        super().__init__(name, health, attack_power, level)
        self.rage = 0

    def attack(self, target):
        self.rage += 5
        print(f"{self.name} performs a heavy warrior attack, rage increases to {self.rage}")
        super().attack(target)

    def power_strike(self, target):
        if self.rage >= 20:
            damage = self.attack_power * 2
            print(f"{self.name} unleashes power strike for {damage} damage")
            target.take_damage(damage)
            self.rage = 0
        else:
            print(f"{self.name} doesn't have enough rage for power strike")


#mage
class Mage(RPGCharacter):
    def __init__(self, name, health, attack_power, level):
        super().__init__(name, health, attack_power, level)
        self.mana = 50

    def take_damage(self, amount):
        reduced = max(amount - 3, 0)
        print(f"{self.name}'s magic shield reduces damage by 3")
        super().take_damage(reduced)

    def cast_spell(self, target):
        if self.mana >= 10:
            damage = self.attack_power + 5
            print(f"{self.name} casts a spell for {damage} damage")
            target.take_damage(damage)
            self.mana -= 10
        else:
            print(f"{self.name} does not have enough mana to cast a spell")


#example
if __name__ == "__main__":
    warrior = Warrior("bob", 120, 15, 5)
    mage = Mage("Jamar Davis-Brown", 80, 12, 5)

    warrior.display_stats()
    mage.display_stats()

    warrior.attack(mage)
    mage.cast_spell(warrior)
    warrior.power_strike(mage)
