class GameCharacter:
    def __init__(self, name, age, ability, hp, status, status_damage_multiplier):
        self.name = name
        self.age = age
        self.ability = ability
        self.hp = hp
        self.status = status
        self.status_damage_multiplier = status_damage_multiplier

    def displayCharacter(self):
        print("Name: {}\nHP: {}\n".format(self.name, self.hp))
