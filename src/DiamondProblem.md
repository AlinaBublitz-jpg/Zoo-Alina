Diagramm: Das Diamond Problem in Python

               A
              / \
             B   C
              \ /
               D

Erklärung: 
Das Diamond-Problem entsteht in Python durch Mehrfachvererbung. 
In diesem Diagramm ist `A` die Basisklasse, von der die Klassen `B` und `C` erben. 
Klasse `D` erbt wiederum sowohl von `B` als auch von `C`. 
Dies führt zu einer diamantenförmigen Vererbungshierarchie.

Problem: 
Wenn `A` eine Methode `m()` definiert, erben sowohl `B` als auch `C` diese Methode. 
Klasse `D` hat nun zwei potenzielle Implementierungen der Methode `m()` aus den Klassen `B` und `C`, 
was zu Mehrdeutigkeiten führt. 
Python löst dieses Problem durch den Einsatz des Method Resolution Order (MRO), 
einer speziellen Reihenfolge, in der Python nach Methoden sucht.



