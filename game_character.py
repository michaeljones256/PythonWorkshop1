class GameCharacter:
    def __init__ (self,name, age, abilites, hp):
        self.name = name
        self.age = age
        self.abilites = abilites
        self.hp = hp
    def displayCharacter(self):
        print("Name: {}\nHP: {}\n".format(self.name, self.hp))
