import random
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = [Spider-Man, Captain America, Iron Man, Thor, Hulk]

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, hero):
        self.heroes.remove(hero)

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
