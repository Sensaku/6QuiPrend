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

    def less_than_board(self, card):
        for ligne in self.lignes:
            if ligne[-1].value < card.value:
                return False
        return True

    def put_in_good_line(self):
        ligne = None
        for action in self.plie:
            if self.less_than_board(action.carte):
                # TODO: à tester!
                ligne = min(self.ligne, key=lambda x: sum(x.cards))
                action.player.score += sum(ligne.cards)
                ligne.cards = [action.carte]
            else:
                # positionner la carte où il faut
                # On cherche la différence absolue entre deux lignes la plus petite
                # Si la carte que l'on veut placer est plus grande, alors on la joue
                # Sinon on en cherche une autre
                for row in self.lignes:
                    if row.cards[-1].value < action.carte.value:
                        pass


    def __repr__(self):
        result = f"Tableau de jeu\n"
        for ligne in self.lignes:
            result += ligne.to_string()
        return result
