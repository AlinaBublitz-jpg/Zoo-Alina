from src.animals.tier import Tier
from abc import ABC, abstractmethod


class Saeugetier(Tier):
    def __init__(self, art, alter, gewicht, fellfarbe):
        super().__init__(art, alter, gewicht)
        self.fellfarbe = fellfarbe

    def saeugen(self):
        print(f"Das {self.get_art()} säugt seine Jungen.")

    def bewegung(self):
        print(f"Das {self.get_art()} läuft auf vier Beinen.")

    def geraeusch(self):
        print(f"Das {self.get_art()} macht Geräusche.")
