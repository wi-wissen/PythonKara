from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 18 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Kara soll bis zu dem Baum laufen. Ist davor eine Beere isst sie diese heimlich.
# Liegt vor dem Baum keine Beere legt sie um den Waldgott zu huldigen eine ab.

move()
