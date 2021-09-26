from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 1 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Führe das folgende Programm aus.

kara.move()
turnRight()
print(mushroomFront())
move()
#turnRight()
print(mushroomFront())
print(treeLeft())
putBerry()
print(onBerry())
removeBerry()
print(onBerry())