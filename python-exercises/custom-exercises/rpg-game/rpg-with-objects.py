"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        return self.health > 0

    def print_status(self):
        print(f'You have {self.health} health and {self.power} power.')

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power

    def alive(self):
        return self.health > 0

    def print_status(self):
        print(f'You have {self.health} health and {self.power} power.')

hero_instance = Hero(10,5)
goblin_instance = Goblin(6,2)

def main(hero,goblin):

    while goblin.alive() > 0 and hero.alive() > 0:
        hero.print_status()
        goblin.print_status()
        print("You have %d health and %d power." % (hero.health, hero.power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            print("You do %d damage to the goblin." % hero.power)
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")

main(hero_instance, goblin_instance)
