from abc import ABC, abstractmethod


# Definiert die abstrakte Klasse Fliegen, die von ABC erbt
class Fliegen(ABC):
    def __init__(self, hoehe, dauer):
        self.hoehe = hoehe
        self.dauer = dauer

    # Abstrakte Methode zur Beschreibung des Fliegens
    @abstractmethod
    def fliegen(self):
        pass




