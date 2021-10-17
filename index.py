from game_character import GameCharacter
from game import Game

def main():
    character1 = GameCharacter("Mario",27,["Fireball"],100)
    character2 = GameCharacter("Lugi",20,["Giant"],100)
    # character1.displayCharacter()

    # Game functions
    # Game.attack(character2)
    # character2.displayCharacter()

    # Loop with attacking
    while(character1.hp > 0 and character2.hp > 0):
        character1_move = input("[{}] Input A for Attack or R for Restore\n".format(character1.name))
        character2_move = input("[{}] Input A for Attack or R for Restore\n".format(character2.name))
        striker = randint(1,2) # Determines who gets to do their move first for each round
        if striker == 1:
            # character 1
            if character1_move == "A":
                Game.attack(character2)
            if character1_move == "R":
                Game.restore(character1)
            # character 2
            if character2_move == "A":
                Game.attack(character1)
            if character2_move == "R":
                Game.restore(character2)

        if striker == 2:
            # character 2
            if character2_move == "A":
                Game.attack(character1)
            if character2_move == "R":
                Game.restore(character2)
            # character 1
            if character1_move == "A":
                Game.attack(character2)
            if character1_move == "R":
               Game.restore(character1)

        character1.displayCharacter()
        character2.displayCharacter()



if __name__ == "__main__":
    main()
