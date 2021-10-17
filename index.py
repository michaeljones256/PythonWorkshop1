from game_character import GameCharacter
from game import Game

def main():
    character1 = GameCharacter("Mario",27,["Fireball"],100)
    character2 = GameCharacter("Lugi",20,["Giant"],100)
    character1.displayCharacter()

    # Game functions
    Game.attack(character2)
    character2.displayCharacter()


if __name__ == "__main__":
    main()
