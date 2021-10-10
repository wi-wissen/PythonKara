from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 7 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Kara begibt sich auf eine heitere Wanderung, die immer geradeaus führt.
# Schau dir untenstehendes Programm und mutmaße, ob Kara gegen den Baum knallen wird.
# Führe das Programm aus und prüfe deine Vermutung.

turnRight()
while True:
    move()
    if(treeFront()):
        break