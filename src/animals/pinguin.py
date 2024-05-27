from src.animals.vogel import Vogel
from src.move.tauchen import Tauchen


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

    def schwimmen(self):
        if self.schwimmfaehigkeit:
            print(f"Der {self.get_art()} kann schwimmen.")
            self.tauchen()
        else:
            print(f"Der {self.get_art()} kann nicht schwimmen.")

    def tauchen(self):
        if self.schwimmfaehigkeit:
            print(f"Der {self.get_art()} taucht bis zu einer Tiefe von {self.tiefe} Metern für {self.dauer} Minuten.")
        else:
            print(f"Der {self.get_art()} kann nicht tauchen, weil er nicht schwimmen kann.")
