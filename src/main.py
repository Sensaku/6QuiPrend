from card import *
from Player import *
from Board import *
from GameEngine import *

# Lib test: - unittest
#           - PyTest

if __name__ == "__main__":

    moteur = Engine()

    for i in range(4):
        moteur.add_player(Player(i))

    moteur.run()

    #carte_test = Card(52,1)
    #print(carte_test)

    #joueur1 = Player("Sandy")
    #joueur1.hand.append(carte_test)

    # plateau = Board()
    # for ligne in plateau.lignes:
    #    ligne.cards.append(Card(14,1))
    #    print(ligne.toString())


    #volontairement cassé
    #joueur1.addCard(3)