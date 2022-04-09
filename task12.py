from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 12 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Kara möchte zwischen den Bäumen Slalom fahren. Der Anfang des Slaloms ist im Bild eingezeichnet.
# Programmiere Kara, so dass sie den Slalom endlos hin- und zurück fährt.
# Der Parcour geht immer um drei Bäume.
