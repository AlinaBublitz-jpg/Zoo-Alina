from src.animals.vogel import Vogel
from src.move.tauchen import Tauchen


# Definiert die Klasse Pinguin, die von den Klassen Vogel und Tauchen erbt
class Pinguin(Vogel, Tauchen):
    def __init__(self, art, alter, gewicht, hoehe, dauer, fluegelspannweite, federn, schwimmfaehigkeit, tiefe,
                 tauchdauer):
        Vogel.__init__(self, art, alter, gewicht, hoehe, dauer, fluegelspannweite, federn)
        Tauchen.__init__(self, tiefe, tauchdauer)
        self.schwimmfaehigkeit = schwimmfaehigkeit

    def bewegung(self):
        print(f"Der {self.get_art()} watschelt.")

    def geraeusch(self):
        print(f"Der {self.get_art()} macht Pinguin-Geräusche.")

    # Methode zur Beschreibung des Schwimmverhaltens des Pinguins
    def schwimmen(self):
        # Überprüft, ob der Pinguin schwimmen kann
        if self.schwimmfaehigkeit:
            # Wenn der Pinguin "schwimmfaehigkeit" besitzt, kann er schwimmmen
            print(f"Der {self.get_art()} kann schwimmen.")
            # Ruft die Methode tauchen auf (wenn er schwimmen kann, kann er auch tauchen)
            self.tauchen()
        else:
            # Gibt aus, dass der Pinguin nicht schwimmen kann
            print(f"Der {self.get_art()} kann nicht schwimmen.")

    # Methode zur Beschreibung des Tauchverhaltens des Pinguins
    def tauchen(self):
        # Überprüft, ob der Pinguin schwimmen kann (wenn er schwimmen kann, kann er auch tauchen)
        if self.schwimmfaehigkeit:
            # Gibt aus, dass der Pinguin taucht, und beschreibt die Tiefe und Dauer
            print(f"Der {self.get_art()} taucht bis zu einer Tiefe von {self.tiefe} Metern für {self.dauer} Minuten.")
        else:
            # Gibt aus, dass der Pinguin nicht tauchen kann, weil er nicht schwimmen kann
            print(f"Der {self.get_art()} kann nicht tauchen, weil er nicht schwimmen kann.")
