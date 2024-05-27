from src.animals.wal import Wal
from src.animals.adler import Adler
from src.animals.chamaeleon import Chamaeleon
from src.animals.loewe import Loewe
from src.animals.pinguin import Pinguin
from src.animals.saeugetier import Saeugetier
from src.animals.vogel import Vogel
from src.animals.reptil import Reptil


# Hauptfunktion, in der die Tiere instanziiert und Methoden aufgerufen werden
def main():
    # Erzeugt Instanzen der verschiedenen Tierklassen
    # Die ersten 3 Werte sind immer "Art", "Alter" und "Gewicht"
    wal = Wal("Wal", 20, 30000, "blau", 500, 30)
    adler = Adler("Adler", 5, 7, 1000, 30, 2.5, "braun und weiß")
    chamaeleon = Chamaeleon("Chamäleon", 2, 0.5, "grün")
    loewe = Loewe("Löwe", 5, 190, "golden")
    pinguin1 = Pinguin("Pinguin", 3, 15, 0, 0, 0.8, "schwarz und weiß", True, 50, 20)
    pinguin2 = Pinguin("Pinguin", 4, 16, 0, 0, 0.9, "schwarz und weiß", True, 55, 25)
    vogel = Vogel("Vogel", 3, 2, 100, 10, 0.5, "bunt")
    reptil = Reptil("Reptil", 4, 10, "schuppig")
    saeugetier = Saeugetier("Säugetier", 5, 60, "braun")
    schaf = Saeugetier("Schaf", 4, 70, "weiß")
    hase = Saeugetier("Hase", 2, 5, "braun")

    # Methodenaufrufe für den Wal
    wal.bewegung()
    wal.geraeusch()
    wal.tauchen()
    wal.besonderheit()
    wal.fuettern(100, "Plankton")
    print(f"Neues Gewicht des Wals: {wal.get_gewicht()} kg")

    # Methodenaufrufe für den Adler
    adler.bewegung()
    adler.geraeusch()
    adler.jagen()
    adler.fuettern(1, "Fleisch")
    adler.fliegen()
    print(f"Neues Gewicht des Adlers: {adler.get_gewicht()} kg")

    # Methodenaufrufe für das Chamäleon
    chamaeleon.bewegung()
    chamaeleon.geraeusch()
    chamaeleon.anpassung("braun")
    chamaeleon.fuettern(0.1, "Insekten")
    print(f"Neues Gewicht des Chamäleons: {chamaeleon.get_gewicht()} kg")

    # Methodenaufrufe für den Löwen
    loewe.bewegung()
    loewe.geraeusch()
    loewe.fuettern(5, "Fleisch")
    print(f"Neues Gewicht des Löwen: {loewe.get_gewicht()} kg")

    # Methodenaufrufe für den ersten Pinguin
    pinguin1.bewegung()
    pinguin1.geraeusch()
    pinguin1.schwimmen()
    pinguin1.tauchen()
    pinguin1.fuettern(2, "Fisch")
    print(f"Neues Gewicht des Pinguins 1: {pinguin1.get_gewicht()} kg")

    # Methodenaufrufe für den zweiten Pinguin
    pinguin2.bewegung()
    pinguin2.geraeusch()
    pinguin2.schwimmen()
    pinguin2.tauchen()
    pinguin2.fuettern(3, "Fisch")
    print(f"Neues Gewicht des Pinguins 2: {pinguin2.get_gewicht()} kg")

    # Methodenaufrufe für den Vogel
    vogel.bewegung()
    vogel.geraeusch()
    vogel.fliegen()
    vogel.fuettern(0.2, "Samen")
    print(f"Neues Gewicht des Vogels: {vogel.get_gewicht()} kg")

    # Methodenaufrufe für das Reptil
    reptil.bewegung()
    reptil.geraeusch()
    reptil.fuettern(0.3, "Insekten")
    print(f"Neues Gewicht des Reptils: {reptil.get_gewicht()} kg")

    # Methodenaufrufe für das Säugetier
    saeugetier.bewegung()
    saeugetier.geraeusch()
    saeugetier.saeugen()
    saeugetier.fuettern(2, "Gras")
    print(f"Neues Gewicht des Säugetiers: {saeugetier.get_gewicht()} kg")

    # Methodenaufrufe für das Schaf
    schaf.bewegung()
    schaf.geraeusch()
    schaf.saeugen()
    schaf.fuettern(3, "Gras")
    print(f"Neues Gewicht des Schafs: {schaf.get_gewicht()} kg")

    # Methodenaufrufe für den Hasen
    hase.bewegung()
    hase.geraeusch()
    hase.saeugen()
    hase.fuettern(0.5, "Karotten")
    print(f"Neues Gewicht des Hasen: {hase.get_gewicht()} kg")

# Prüft, ob das Skript direkt ausgeführt wird, und ruft in diesem Fall die main-Funktion auf
if __name__ == '__main__':
    main()
