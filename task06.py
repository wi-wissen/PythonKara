from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 6 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Kara sucht ihre Erdbeeren. Schreibe eine Wiederholung, sodass Kara die unabhängig von der Entfernung immer auf einer Erdbeere sitzen bleibt.

turnRight()