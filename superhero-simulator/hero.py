# hero.py
import random
from ability import Ability
from armor import Armor

class Hero:
    # we want hero to have a default starting health, by default is 100
    def __init__(self, name, kills = 0, deaths = 0, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armors = []
        self.abilities = []
        self.weapons = []
        self.deaths = kills
        self.kills = deaths


    def battle(self,opponent):
        self.opponent = opponent
        winner = random.choice([self, opponent])
        print(f'The winner is {winner.name}')
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def sum_of_attacks(self):
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()
            
        return total_damage
    
    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0

        for armor in self.armors:
            total_block += armor.block()

        return total_block
    
    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_kill(self, kills_number):
        self.kills += kills_number
        return self.kills
    
    def add_death(self, deaths_number):
        self.deaths += deaths_number
        return self.deaths
