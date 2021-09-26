from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 14 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Programmiere Kara so, dass sie die Spur von Erdbeeren "auffrisst"! Da du weißt, dass die Spur nie entlang eines Baumes geht, kann das Programm beendet werden, sobald Kara auf Erdbeeren vor einem Baum steht.

