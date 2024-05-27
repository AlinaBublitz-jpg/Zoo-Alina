from src.animals.vogel import Vogel


class Adler(Vogel):
    def __init__(self, art, alter, gewicht, hoehe, dauer, fluegelspannweite, federn):
        super().__init__(art, alter, gewicht, hoehe, dauer, fluegelspannweite, federn)

    def bewegung(self):
        print(f"Der {self.get_art()} schwebt majestätisch in der Luft.")

    def geraeusch(self):
        print(f"Der {self.get_art()} stößt einen durchdringenden Schrei aus.")

    def jagen(self):
        print(f"Der {self.get_art()} stürzt sich mit hoher Geschwindigkeit auf seine Beute.")
