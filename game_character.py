class GameCharacter:
    def __init__ (self,name, age, ability, hp, status):
        self.name = name
        self.age = age
        self.ability = ability
        self.hp = hp
        self.status = status
    def displayCharacter(self):
        print("Name: {}\nHP: {}\n".format(self.name, self.hp))
