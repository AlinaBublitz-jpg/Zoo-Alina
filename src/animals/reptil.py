from src.animals.tier import Tier


class Reptil(Tier):
    def __init__(self, art, alter, gewicht, schuppen):
        super().__init__(art, alter, gewicht)
        self._schuppen = schuppen

    def get_schuppen(self):
        return self._schuppen

    def set_schuppen(self, schuppen):
        self._schuppen = schuppen

    def bewegung(self):
        print(f"Das {self.get_art()} kriecht.")

    def geraeusch(self):
        print(f"Das {self.get_art()} zischt.")