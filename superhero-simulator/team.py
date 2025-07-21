# team.py
from hero import Hero

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, new_hero):
        self.heroes.append(new_hero)
    
    def remove_hero(self, delete_hero):
        try:
            self.heroes.remove(delete_hero)
        except:
            print('The hero you entered does not exist in the team')

    def list_heroes(self):
        for hero in self.heroes:
            print(hero)

    def total_kills(self):
        total_k = 0
        for hero in self.heroes:
            total_k += Hero.kills
        return total_k
    
    def total_deaths(self):
        total_d = 0
        for hero in self.heroes:
            total_k += Hero.deaths
        return total_d