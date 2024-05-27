from abc import ABC, abstractmethod


class Tier(ABC):
    def __init__(self, art, alter, gewicht):
        self.__art = art  # privates Attribut
        self.alter = alter
        self._gewicht = gewicht  # geschütztes Attribut

    # Getter-Methode für das private Attribut art
    def get_art(self):
        return self.__art

    # Setter-Methode für das private Attribut art
    def set_art(self, art):
        self.__art = art

    # Getter-Methode für das geschützte Attribut gewicht
    def get_gewicht(self):
        return self._gewicht

    # Setter-Methode für das geschützte Attribut gewicht
    def set_gewicht(self, gewicht):
        self._gewicht = gewicht

    @abstractmethod
    def bewegung(self):
        pass

    @abstractmethod
    def geraeusch(self):
        pass

    def fuettern(self, futtermenge, futtertyp=None):
        self._gewicht += futtermenge
        if futtertyp:
            print(f"Das Tier wird mit {futtermenge} kg {futtertyp} gefüttert.")
        else:
            print(f"Das Tier wird mit {futtermenge} kg gefüttert.")
