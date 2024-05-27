from src.animals.pinguin import Pinguin

# Erstellung eines Pinguin-Objekts
pinguin1 = Pinguin("Pinguin", 3, 15, 10, 5, 15, "schwarz und weiß", 12, 10, 17)

# Verweis von pinguin2 auf dasselbe Pinguin-Objekt
pinguin2 = pinguin1

# Anzeige des Gewichts beider Verweise
print(f"Gewicht von pinguin1 vor dem Füttern: {pinguin1.gewicht} kg")
print(f"Gewicht von pinguin2 vor dem Füttern: {pinguin2.gewicht} kg")

# Ändern des Zustands des Pinguin-Objekts über pinguin1
pinguin1.fuettern(2)

# Anzeige des Gewichts beider Verweise nach dem Füttern
print(f"Gewicht von pinguin1 nach dem Füttern: {pinguin1.gewicht} kg")
print(f"Gewicht von pinguin2 nach dem Füttern: {pinguin2.gewicht} kg")
