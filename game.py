from random import randint

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
        character.hp = character.hp + randint(1,10)
        if character.hp > 100:
            character.hp = 100

    def status_damage(defender):
        if defender.status == "burned":
            defender.hp = defender.hp - randint(3,10) * defender.status_damage_multiplier()
            defender.status_damage_multiplier += 1.5
        if defender.status == "frozen":
            defender.hp = defender.hp - randint(3,10) * defender.status_damage_multiplier()
            defender.status_damage_multiplier += 1.5
