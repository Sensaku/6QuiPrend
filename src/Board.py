class Ligne:
    def __init__(self):
        self.cards = []

    def to_string(self):
        result = ""
        for case in self.cards:
            result += case.to_string()
        return result


class Board:

    def __init__(self):
        self.lignes = []
        self.plie = []
        for i in range(4):
            self.lignes.append(Ligne())

    def init_board(self, cards):
        for ligne in self.lignes:
            ligne.cards.append(cards.pop())

    def __repr__(self):
        result = f"Tableau de jeu\n"
        for ligne in self.lignes:
            result += ligne.to_string()
        return result
