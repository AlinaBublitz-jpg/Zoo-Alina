
from src.move.fliegen import Fliegen
from src.animals.tier import Tier

# Definiert die Klasse Vogel, die von den Klassen Tier und Fliegen erbt
class Vogel(Tier, Fliegen):
    def __init__(self, art, alter, gewicht, hoehe, dauer, fluegelspannweite, federn):
        Tier.__init__(self, art, alter, gewicht)
        Fliegen.__init__(self, hoehe, dauer)
        self.fluegelspannweite = fluegelspannweite
        self.federn = federn

    def bewegung(self):
        print(f"Der {self.get_art()} bewegt sich durch die Luft.")

    def geraeusch(self):
        print(f"Der {self.get_art()} zwitschert.")

    def fliegen(self):
        print(f"Der {self.get_art()} fliegt in einer Höhe von {self.hoehe} Metern für {self.dauer} Minuten.")
