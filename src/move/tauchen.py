from abc import ABC, abstractmethod


class Tauchen(ABC):
    def __init__(self, tiefe, dauer):
        self.tiefe = tiefe
        self.dauer = dauer

    @abstractmethod
    def tauchen(self):
        pass
