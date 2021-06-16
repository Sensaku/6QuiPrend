from card import *
from Player import *

if __name__ == "__main__":

    carte_test = Card(52,1)
    print(carte_test)

    joueur1 = Player("Sandy")
    joueur1.hand.append(carte_test)

    #volontairement cassé
    #joueur1.addCard(3)
    print(joueur1)