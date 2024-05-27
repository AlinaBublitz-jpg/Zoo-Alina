from src.animals.reptil import Reptil


# Definiert die Klasse Chamaeleon, die von der Klasse Reptil erbt
class Chamaeleon(Reptil):
    def __init__(self, art, alter, gewicht, schuppen):
        super().__init__(art, alter, gewicht, schuppen)

    # Methode zur Anpassung der Schuppenfarbe des Chamäleons
    def anpassung(self, neue_farbe):
        # Setzt die neue Schuppenfarbe
        self.set_schuppen(neue_farbe)
        # Gibt aus, dass das Chamäleon seine Schuppenfarbe angepasst hat
        print(f"Das Chamäleon passt seine Schuppenfarbe an {self.get_schuppen()} an.")

    def bewegung(self):
        print(f"Das Chamäleon bewegt sich langsam und vorsichtig.")

    def geraeusch(self):
        print(f"Das Chamäleon macht leise Geräusche.")
