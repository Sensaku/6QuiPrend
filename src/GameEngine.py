from Board import *
from card import *
import random


class Engine:

    def __init__(self):
        self.board = None
        self.deck = []
        self.players = []

    def initilisation(self):
        self.board = Board()

    def generate_card(self):

        for i in range(1, 105):

            if i % 11 == 0:
                self.deck.append(Card(i, 5))
            elif i % 10 == 0:
                self.deck.append(Card(i, 3))
            elif i % 5 == 0:
                self.deck.append(Card(i, 2))
            else:
                self.deck.append(Card(i, 1))

        random.shuffle(self.deck)

    def give_hand(self):
        for i in range(10):
            for player in self.players:
                player.hand.append(self.deck.pop())

    def add_player(self, player):
        self.players.append(player)

    def ask_player_to_choose(self):
        for player in self.players:
            self.board.plie.append(player.choose_card())
        # Redonner une carte dans le tas de carte

    def apply_turn(self):
        self.board.plie.sort(key=lambda x: x.carte.value)
        self.board.put_in_good_line()

    def run(self):
        self.initilisation()
        self.generate_card()
        self.give_hand()
        to_board = [self.deck.pop() for i in range(4)]

        self.board.init_board(to_board)
        print(self.board)
        print()

        self.ask_player_to_choose()
        self.apply_turn()
        print(f"Tour de jeu:\n{self.board}")