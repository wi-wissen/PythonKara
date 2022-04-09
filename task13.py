from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 13 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Das vorherige Programm Slalom sollte mehrere gleiche Teile enthalten, nämlich für das Herumgehen um jeden Baum.
# Um das oberste Prinzip der Programmierer Never repeat yourself! zu realisieren, werden wir zwei neue Funktionen erschaffen.
# Kopiere dein Programm aus der letzten Aufgabe und schreibe die halbe Umrundung eines Baums in die Funktion.
# Verwende diese nun anschließend um wieder Slalom zu fahren.

def halbkreis():
    print("Hier drehe ich eine halbe Runde!")
    # Hier kommt deine Funktion hin.