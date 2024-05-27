from abc import ABC, abstractmethod

# Definiert die abstrakte Klasse Tauchen, die von ABC erbt
class Tauchen(ABC):
    def __init__(self, tiefe, dauer):
        self.tiefe = tiefe
        self.dauer = dauer

    # Abstrakte Methode zur Beschreibung des Tauchens
    @abstractmethod
    def tauchen(self):
        pass
