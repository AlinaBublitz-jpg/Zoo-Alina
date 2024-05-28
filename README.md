# Zoo-Alina

Dieses Projekt simuliert verschiedene Tiere in einem Zoo. 
Es verwendet Objektorientierte Programmierung in Python, um die Eigenschaften und Methoden der Tiere zu modellieren. 
Das Projekt umfasst verschiedene Tierklassen und ermöglicht die Interaktion mit den Tieren durch Methoden wie geraeusch, bewegung und fuettern.


**Installation**

Stellen Sie sicher, dass Python 3.x installiert ist. 



**Projektstruktur und Klassen**

**animals Paket**

tier.py: Enthält die Basisklasse Tier, die abstrakte Methoden für Bewegung und Geräusch definiert.

saeugetier.py: Erweitert Tier um die Klasse Saeugetier mit spezifischen Eigenschaften und Methoden.

vogel.py: Erweitert Tier um die Klasse Vogel, die auch die Klasse Fliegen aus dem move Paket verwendet.


reptil.py: Erweitert Tier um die Klasse Reptil.

adler.py: Definiert die Klasse Adler, die von Vogel erbt und eine spezielle Methode jagen enthält.

chamaeleon.py: Definiert die Klasse Chamaeleon, die von Reptil erbt und die Methode anpassung enthält.

loewe.py: Definiert die Klasse Loewe, die von Saeugetier erbt.

pinguin.py: Definiert die Klasse Pinguin, die von Vogel und Tauchen erbt und eine spezielle Methode schwimmen enthält.

wal.py: Definiert die Klasse Wal, die von Saeugetier und Tauchen erbt.



**move Paket**

tauchen.py: Definiert die abstrakte Klasse Tauchen.

fliegen.py: Definiert die abstrakte Klasse Fliegen.



**Unit-Tests**

Die Unit-Tests befinden sich im Verzeichnis tests und testet die Methoden geraeusch und fuettern für alle Tierklassen.

