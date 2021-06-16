from card import Card


class Player:

    def __init__(self, name: str):
        self.hand = []
        self.name = name

    def get_Hand(self):
        return self.hand

    def set_Hand(self, hand: list):
        self.hand = hand

    def add_Card(self, card: Card):
        """
        Méthode qui permet d'ajouter une carte
        :param card:
        :return:
        """
        if isinstance(card, Card):
            self.hand.append(card)
        else:
            raise NotImplementedError("Mauvaise instance de carte")



    def __repr__(self):
        return f"Nom: {self.name}\nMain: {self.hand}"