import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100): # starting_health=100 makes the starting_health arguement OPTIONAL
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.weapons =[]
    
    def battle(self, opponent):
        my_list = [self.name, opponent.name] 
        print(random.choice(my_list))
    
    def add_ability(self, ability):
        self.abilities.append(ability)
        print(self.abilities)

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        for weapon in self.weapons:
            total_damage += weapon.attack()
        print (total_damage)
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        blocked = self.defend()
        actual_damage = max(damage - blocked, 0)
        self.current_health -= actual_damage
        if self.current_health < 0:
            self.current_health = 0
        return actual_damage





if __name__ == "__main__":
    my_hero = Hero("Spider-Man", 150) #150 is our starting health.
    print(my_hero.name)
    print(my_hero.current_health)
    my_opponent = Hero("Captain America", 200)
    my_hero.battle(my_opponent)
    my_hero.add_ability("Web Shooter")
    my_hero.add_ability("Spidey Senses")
    my_hero.add_armor(Armor("Helmet", 10))
    my_hero.add_armor(Armor("Shield", 40))
    my_hero.defend()
    my_hero.take_damage(30)
    print(my_hero.current_health)
    my_hero.add_weapon(Weapon("Lazer", 30))
