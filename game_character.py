class GameCharacter:
    def __init__ (self,name, age, abilites, hp):
        self.name = name
        self.age = age
        self.abilites = abilites
        self.hp = hp
    def displayCharacter(self):
        print("Name: {}\nAge: {}\nHP: {}\nAbilties:".format(self.name, self.age, self.hp))
        for ability in self.abilites:
            print("- " + ability)
