# weapon.py

from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        '''Return a random value between half and full max_damage'''
        half_damage = self.max_damage // 2
        return random.randint(half_damage, self.max_damage)
    
if __name__ == "__main__":
    sword = Weapon("Wood sword", 100)
    print(f"{sword.name} attack: {sword.attack()}")
    print(f"{sword.name} attack: {sword.attack()}")
    print(f"{sword.name} attack: {sword.attack()}")
