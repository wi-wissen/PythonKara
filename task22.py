from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 22 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Führe Kara durch das Labyrinth zu den Erdbeeren.
# Jede horizontale Baumreihe, außer der Untersten, hat genau einen Ausgang, der in die nächst höhere Zeile führt.
# Diesen muss Kara jeweils finden. Hinter dem letzten Ausgang wartet das Kleeblatt auf sie.
# Programmiere Kara so, dass sie die Erdbeeren findet und aufnimmt. Dabei soll sie nie an ihrem Ausgang vorbeilaufen, ohne ihn zu benutzen!
# Zu Beginn schaut Kara immer nach rechts.

turnRight
