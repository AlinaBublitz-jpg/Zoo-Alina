import unittest
from io import StringIO
import sys
from src.animals.wal import Wal
from src.animals.adler import Adler
from src.animals.chamaeleon import Chamaeleon
from src.animals.loewe import Loewe
from src.animals.pinguin import Pinguin
from src.animals.saeugetier import Saeugetier
from src.animals.vogel import Vogel
from src.animals.reptil import Reptil


# Definiert die Testklasse, die von unittest.TestCase erbt
class TestTiere(unittest.TestCase):
    # Setzt die Testumgebung auf, indem Instanzen der Tierklassen erstellt werden
    def setUp(self):
        self.wal = Wal("Wal", 20, 30000, "blau", 500, 30)
        self.adler = Adler("Adler", 5, 7, 1000, 30, 2.5, "braun und weiß")
        self.chamaeleon = Chamaeleon("Chamäleon", 2, 0.5, "grün")
        self.loewe = Loewe("Löwe", 5, 190, "golden")
        self.pinguin = Pinguin("Pinguin", 3, 15, 0, 0, 0.8, "schwarz und weiß", True, 50, 20)
        self.saeugetier = Saeugetier("Säugetier", 5, 60, "braun")
        self.vogel = Vogel("Vogel", 3, 2, 100, 10, 0.5, "bunt")
        self.reptil = Reptil("Reptil", 4, 10, "schuppig")

    # Testet die geräusch-Methode für alle Tiere
    def test_geraeusch(self):
        # Erstellt eine Liste von Tupeln, die jeweils ein Tier und das erwartete Geräusch enthalten
        animals = [
            (self.wal, "Der Wal macht Walgesänge."),
            (self.adler, "Der Adler stößt einen durchdringenden Schrei aus."),
            (self.chamaeleon, "Das Chamäleon macht leise Geräusche."),
            (self.loewe, "Der Löwe brüllt laut."),
            (self.pinguin, "Der Pinguin macht Pinguin-Geräusche."),
            (self.saeugetier, "Das Säugetier macht Geräusche."),
            (self.vogel, "Der Vogel zwitschert."),
            (self.reptil, "Das Reptil zischt.")
        ]

        # Iteriert über jedes Tier und das erwartete Geräusch
        for animal, expected_sound in animals:
            # Führt einen Subtest für jedes Tier durch
            with self.subTest(animal=animal.get_art()):
                captured_output = StringIO()
                sys_stdout = sys.stdout  # Speichern des ursprünglichen sys.stdout
                sys.stdout = captured_output  # sys.stdout auf StringIO umleiten
                animal.geraeusch()  # Ruft die geräusch-Methode des Tieres auf
                sys.stdout = sys_stdout  # Wiederherstellen des ursprünglichen sys.stdout
                output = captured_output.getvalue().strip()
                try:
                    # Überprüft, ob das erwartete Geräusch in der Ausgabe enthalten ist
                    self.assertIn(expected_sound, output)
                    print(f"Die Methode geräusch für {animal.get_art()} funktioniert korrekt.")
                except AssertionError as e:
                    # Gibt eine Fehlermeldung aus, wenn die Überprüfung fehlschlägt, und wirft die AssertionError
                    print(
                        f"Die Methode geräusch für {animal.get_art()} funktioniert nicht korrekt. Erwartet: '{expected_sound}', aber erhalten: '{output}'")
                    raise e

    # Testet die füttern-Methode für alle Tiere
    def test_fuettern(self):
        # Erstellt eine Liste von Tupeln, die jeweils ein Tier, die Futtermenge und den Futtertyp enthalten
        animals = [
            (self.wal, 100, "Plankton"),
            (self.adler, 1, "Fleisch"),
            (self.chamaeleon, 0.1, "Insekten"),
            (self.loewe, 5, "Fleisch"),
            (self.pinguin, 2, "Fisch"),
            (self.saeugetier, 2, "Gras"),
            (self.vogel, 0.2, "Samen"),
            (self.reptil, 0.3, "Insekten")
        ]

        # Iteriert über jedes Tier, die Futtermenge und den Futtertyp
        for animal, futtermenge, futtertyp in animals:
            # Führt einen Subtest für jedes Tier durch
            with self.subTest(animal=animal.get_art()):
                initial_gewicht = animal.get_gewicht()
                animal.fuettern(futtermenge, futtertyp)
                try:
                    # Überprüft, ob das Gewicht des Tieres korrekt aktualisiert wurde
                    self.assertEqual(animal.get_gewicht(), initial_gewicht + futtermenge)
                    print(
                        f"Die Methode füttern für {animal.get_art()} funktioniert korrekt. Das Gewicht wurde richtig angepasst.")
                except AssertionError as e:
                    # Gibt eine Fehlermeldung aus, wenn die Überprüfung fehlschlägt, und wirft die AssertionError
                    print(
                        f"Die Methode füttern für {animal.get_art()} funktioniert nicht korrekt. Erwartet: {initial_gewicht + futtermenge}, aber erhalten: {animal.get_gewicht()}")
                    raise e

                # Testet die füttern-Methode ohne Angabe des Futtertyps
                initial_gewicht = animal.get_gewicht()
                animal.fuettern(futtermenge)
                try:
                    # Überprüft, ob das Gewicht des Tieres erneut korrekt aktualisiert wurde
                    self.assertEqual(animal.get_gewicht(), initial_gewicht + futtermenge)
                    print(
                        f"Die Methode füttern ohne Angabe des Futtertyps für {animal.get_art()} funktioniert korrekt. Das Gewicht wurde richtig angepasst.")
                except AssertionError as e:
                    # Gibt eine Fehlermeldung aus, wenn die Überprüfung fehlschlägt, und wirft die AssertionError
                    print(
                        f"Die Methode füttern ohne Angabe des Futtertyps für {animal.get_art()} funktioniert nicht korrekt. Erwartet: {initial_gewicht + futtermenge}, aber erhalten: {animal.get_gewicht()}")
                    raise e


# Führt die Tests aus, wenn das Skript direkt ausgeführt wird
if __name__ == '__main__':
    unittest.main()
