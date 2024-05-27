from src.animals.tier import Tier

# Definiert die Klasse Reptil, die von der Klasse Tier erbt
class Reptil(Tier):
    def __init__(self, art, alter, gewicht, schuppen):
        super().__init__(art, alter, gewicht)
        self._schuppen = schuppen

    # Methode, um die Schuppen des Reptils zu erhalten
    def get_schuppen(self):
        return self._schuppen

    # Methode, um die Schuppen des Reptils zu setzen
    def set_schuppen(self, schuppen):
        self._schuppen = schuppen

    def bewegung(self):
        print(f"Das {self.get_art()} kriecht.")

    def geraeusch(self):
        print(f"Das {self.get_art()} zischt.")