from src.animals.saeugetier import Saeugetier


# Definiert die Klasse Löwe, die von der Klasse Säugetier erbt
class Loewe(Saeugetier):
    def bewegung(self):
        print("Der Löwe schleicht durch sein Gehege.")

    # Geräusch des Löwens
    def geraeusch(self):
        print("Der Löwe brüllt laut.")
