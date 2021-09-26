from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 13 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Das vorherige Programm Slalom sollte mehrere gleiche Teile enthalten, nämlich für das Herumgehen um jeden Baum. Um das oberste Prinzip der Programmierer Never repeat yourself! zu realisieren, werden wir zwei neue Funktionen erschaffen. Schreibe zwischen die geschweiften Klammern der Funktion die Befehle, die es braucht, um um den Baum zu biegen. Verwende diese nun anschließend um wieder Slalom zu fahren.

turnRight()