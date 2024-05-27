from abc import ABC, abstractmethod


class Fliegen(ABC):
    def __init__(self, hoehe, dauer):
        self.hoehe = hoehe
        self.dauer = dauer

    @abstractmethod
    def fliegen(self):
        pass
