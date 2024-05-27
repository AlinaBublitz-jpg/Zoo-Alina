from src.animals.saeugetier import Saeugetier
from src.move.tauchen import Tauchen


class Wal(Saeugetier, Tauchen):
    def __init__(self, art, alter, gewicht, fellfarbe, tiefe, dauer):
        Saeugetier.__init__(self, art, alter, gewicht, fellfarbe)
        Tauchen.__init__(self, tiefe, dauer)

    def bewegung(self):
        print(f"Der {self.get_art()} schwimmt im Wasser.")

    def geraeusch(self):
        print(f"Der {self.get_art()} macht Walgesänge.")

    def tauchen(self):
        print(f"Der {self.get_art()} taucht bis zu einer Tiefe von {self.tiefe} Metern für {self.dauer} Minuten.")

    def besonderheit(self):
        print(f"Ich bin ein {self.get_art()} und zähle zu den einzigen Säugetieren, die unter Wasser leben.")
