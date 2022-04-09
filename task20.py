from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 20 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Schon wieder Slaloms? Ja, aber diesmal musst du variabel sein.
# Erweitere dein Programm aus der vorherigen Slalomaufgabe so, dass Kara selbst erkennt, wie viele Bäume umkreist werden sollen.

move()
