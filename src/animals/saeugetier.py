from src.animals.tier import Tier
from abc import ABC, abstractmethod


# Definiert die Klasse Saeugetier, die von der Klasse Tier erbt
class Saeugetier(Tier):
    def __init__(self, art, alter, gewicht, fellfarbe):
        super().__init__(art, alter, gewicht)
        self.fellfarbe = fellfarbe

    # Methode zur Beschreibung des Säugens der Jungen durch das Säugetier
    def saeugen(self):
        print(f"Das {self.get_art()} säugt seine Jungen.")

    def bewegung(self):
        print(f"Das {self.get_art()} läuft auf vier Beinen.")

    # Geräusch des Säugetiers
    def geraeusch(self):
        print(f"Das {self.get_art()} macht Geräusche.")
