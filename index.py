from game_character import GameCharacter
from game import Game
from random import randint
def main():
    character1 = GameCharacter("Mario",27,"burned",100,"")
    character2 = GameCharacter("Lugi",20,"frozen",100,"")
    # character1.displayCharacter()

    # Loop with attacking
    while(character1.hp > 0 and character2.hp > 0):
        character1_move = input("[{}] Input A for Attack, S for Special Attack, or R for Restore\n".format(character1.name))
        character2_move = input("[{}] Input A for Attack, S for Special Attack, or R for Restore\n".format(character2.name))
        striker = randint(1,2) # Determines who gets to do their move first for each round
        # If character 1 is picked to go first
        if striker == 1:
        # character 1
            if character1_move == "A":
                print("[{}] Attacks {}".format(character1.name, character2.name))
                Game.attack(character2)
            if character1_move == "S":
                print("[{}] Special Attacks {}".format(character1.name, character2.name))
                Game.special_attack(character1, character2)
            if character1_move == "R":
                print("[{}] Restores their".format(character1.name))
                Game.restore(character1)
            if character2.status:
                print("[{}] Damaged by {}".format(character1.name, character1.status))
                Game.status_damage(character1)
            if character2.hp <= 0:
                print("{} has died, {} wins!".format(character2.name, character1.name))
                break
        # character 2
            if character2_move == "A":
                print("[{}] Attacks {}".format(character2.name, character1.name))
                Game.attack(character1)
            if character1_move == "S":
                print("[{}] Special Attacks {}".format(character2.name, character1.name))
                Game.special_attack(character2, character1)
            if character2_move == "R":
                print("[{}] Restores their".format(character2.name))
                Game.restore(character2)
                # Checks if they have a special status to damage them
            if character1.status:
                print("[{}] Damaged by {}".format(character1.name, character1.status))
                Game.status_damage(character1)
            if character1.hp <= 0:
                print("{} has died, {} wins!".format(character1.name, character2.name))
                break

        #If characer 2 goes first
        if striker == 2:
        # character 2
            if character2_move == "A":
                print("[{}] Attacks {}".format(character2.name, character1.name))
                Game.attack(character1)
            if character2_move == "S":
                print("[{}] Special Attacks {}".format(character2.name, character1.name))
                Game.special_attack(character2, character1)
            if character2_move == "R":
                print("[{}] Restores their".format(character2.name))
                Game.restore(character2)
                # Checks if they have a special status to damage them
            if character1.status:
                print("[{}] Damaged by {}".format(character1.name, character1.status))
                Game.status_damage(character1)
            if character1.hp <= 0:
                print("{} has died, {} wins!".format(character1.name, character2.name))
                break

        # character 1
            if character1_move == "A":
                print("[{}] Attacks {}".format(character1.name, character2.name))
                Game.attack(character2)
            if character1_move == "S":
                print("[{}] Special Attacks {}".format(character1.name, character2.name))
                Game.special_attack(character1, character2)
            if character1_move == "R":
                print("[{}] Restores their".format(character1.name))
                Game.restore(character1)
                # Checks if they have a special status to damage them
            if character2.status:
                print("[{}] Damaged by {}".format(character2.name, character2.status))
                Game.status_damage(character2)
            if character2.hp <= 0:
                print("{} has died, {} wins!".format(character1.name, character2.name))
                break




        print("[{}] Health: {}".format(character1.name, character1.hp))
        print("[{}] Health: {}".format(character2.name, character2.hp))
    # character1.displayCharacter()
    # character2.displayCharacter()



if __name__ == "__main__":
    main()
