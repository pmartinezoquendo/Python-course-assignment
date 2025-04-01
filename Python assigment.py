# CLASS REQUIREMENTS

# Create a Character class with the following parameters (self, name, health, energy, experience, and level).
class Character:
    def __init__(self, name, health, energy, experience, level):
        self.name = name
        self.health = health
        self.energy = energy
        self.experience = experience
        self.level = level

    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to level {self.level}!")

    def hero_attacks_monster(self, target):
        if self.energy >= 5:
            self.energy -= 5
            self.experience += 1
            print(f"{self.name} attacks {target.name}!")
            target.health -= 10
            print(f"{target.name}'s health reduced to {target.health}.")
            if self.experience % 5 == 0:
                self.level_up()
        else:
            print(f"{self.name} doesn't have enough energy to attack.")
            
    def monster_attacks_hero(self, target): # Added 'target' parameter
        if self.energy >= 10:
            self.energy -= 10
            print(f"{self.name} attacks {target.name}!")
            target.health -= 15 # Deduct 15 health from the target (hero)
            print(f"{target.name}'s health reduced to {target.health}.")
    


# Create a monster attack function that each time it is called, it takes away 10 energy
# points from the monster.
def monster_attack(monster):
  monster.energy -= 10

# GAMEPLAY FUNCTION

# 11. Print hero’s stats and monster’s stats.

def gameplay():
    # Create a Python hero object.
    hero = Character("hero", 100, 100, 0, 1)

    # Create a Java monster object.
    monster = Character("monster", 100, 100, 10, 3)

    print(f"{hero.name}: Health: {hero.health}, Energy: {hero.energy}, Experience: {hero.experience}, Level: {hero.level}")
    print(f"{monster.name}: Health: {monster.health}, Energy: {monster.energy}, Experience: {monster.experience}, Level: {monster.level}")

# 12. Create the main while loop and print hero’s options 
# (Attack and Run).

    while True:
        print("attack or run?")
        choice = input("Enter attack or run: ").lower().strip()
        if choice == 'attack':
            #hero attaks monster
            hero.hero_attacks_monster(monster)

            #does the monster attack back? if so:
            monster.monster_attacks_hero(hero)

            # program has to check for health of the hero and monster to make sure they're both still "alive"
            if hero.health <= 20:
                print("Warning! Hero's health is less than 20 points.")
            if hero.health <= 0:
                print("Hero is defeated.")
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again == "yes":
                    # create a new monster, ie. monster = Character(...)
                    monster = Character("monster", 100, 100, 10, 3)
                    # maybe the hero gets more energy and/or health
                    hero = Character("hero", 100, 100, 0, 1)
                    pass
                elif play_again == "no":
                    print("Thanks for playing!")
                    break
            # if monster is dead, ask if the user wants to play again with a new monster
            if monster.health <= 0:
                print("Monster has been defeated.")
                hero.experience += 10 
                print(f"{hero.name} gained 10 experience points!")
            # if the hero is dead, ask if the user wants to play again and start over
            
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again == "yes":
                    # create a new monster, ie. monster = Character(...)
                    monster = Character("monster", 100, 100, 10, 3)
                    # maybe the hero gets more energy and/or health
                    hero.energy += 20
                    hero.health += 15
                    pass
                elif play_again == "no":
                    print("Thanks for playing!")
                    break
            pass
        elif choice == 'run':
            print("Game over")
            break
        else:
            print("Invalid choice. Please enter attack or run.")

"""
# 18. If hero kills monster, hero gets 10 experience points.

if monster.health <= 0:
  hero.experience += 10 
  print(f"{hero.name} gained 10 experience points!")



# 20. Each time the hero kills monster, game asks if player wants to play again.

""
        """

gameplay()