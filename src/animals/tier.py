from abc import ABC, abstractmethod


# Definiert die abstrakte Klasse Tier, die von ABC erbt
class Tier(ABC):
    def __init__(self, art, alter, gewicht):
        self.__art = art  # privates Attribut, das die Art des Tieres speichert
        self.alter = alter # öffentliches Attribut, das das Alter des Tieres speichert
        self._gewicht = gewicht  # geschütztes Attribut, das das Gewicht des Tieres speichert


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
        passA

    # Methode zur Beschreibung des Fütterns des Tieres
    def fuettern(self, futtermenge, futtertyp=None):
        # Erhöht das Gewicht des Tieres um die Futtermenge
        self._gewicht += futtermenge
        if futtertyp: # es können unteschiedliche Parameter gegeben werden - wird hier geprüft
            # Gibt aus, dass das Tier mit der angegebenen Menge und Art von Futter gefüttert wird
            print(f"Das Tier wird mit {futtermenge} kg {futtertyp} gefüttert.")
        else:
            # Gibt aus, dass das Tier mit der angegebenen Menge von Futter gefüttert wird
            print(f"Das Tier wird mit {futtermenge} kg gefüttert.")

    @property
    def gewicht(self):
        return self._gewicht
