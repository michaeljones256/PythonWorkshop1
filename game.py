from random import randint
from random import uniform

class Game:
    def __init__ (self,name, description, characters):
        self.gameName = name
        self.gameDescription = description
        self.character = characters
    def attack(defender):
        defender.hp = defender.hp - randint(5,30)
    def special_attack(attacker, defender):
        defender.status = attacker.ability
    def restore(character):
        character.status = None
        character.status_damage_multiplier = 0
        character.hp = character.hp + randint(1,10)
        if character.hp > 100:
            character.hp = 100


    def status_damage(defender):
        if defender.status == "burned":
            defender.status_damage_multiplier += uniform(1.1,1.9)
            temp = randint(3,10) * defender.status_damage_multiplier
            defender.hp = defender.hp - temp
            print("[{}] takes {} damage from {}".format(defender.name,temp,defender.status))

            
        if defender.status == "frozen":
            defender.status_damage_multiplier += uniform(1.1,1.9)
            temp = randint(3,10) * defender.status_damage_multiplier
            defender.hp = defender.hp - temp
            print("[{}] takes {} damage from {}".format(defender.name,temp,defender.status))
