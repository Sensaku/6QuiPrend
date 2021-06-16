class Card:

    def __init__(self, value, score):
        self.value = value
        self.score = score

    def get_value(self):
        return self.value

    def get_score(self):
        return self.score

    def __repr__(self):
        return f"valeur: {self.value}\tScore: {self.score}"