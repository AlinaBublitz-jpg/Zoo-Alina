from src.animals.reptil import Reptil


class Chamaeleon(Reptil):
    def __init__(self, art, alter, gewicht, schuppen):
        super().__init__(art, alter, gewicht, schuppen)

    def anpassung(self, neue_farbe):
        self.set_schuppen(neue_farbe)
        print(f"Das Chamäleon passt seine Schuppenfarbe an {self.get_schuppen()} an.")

    def bewegung(self):
        print(f"Das Chamäleon bewegt sich langsam und vorsichtig.")

    def geraeusch(self):
        print(f"Das Chamäleon macht leise Geräusche.")
