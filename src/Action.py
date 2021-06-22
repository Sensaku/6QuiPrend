class PlayerAction:

    def __init__(self, joueur, carte):
        self.joueur = joueur
        self.carte = carte

    def __repr__(self):
        return f"Le joueur {self.joueur} a joué {self.carte}"