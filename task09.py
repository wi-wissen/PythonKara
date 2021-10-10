from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 9 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Kara sucht Erdbeeren. Sie weiß, dass welche geradeaus vor ihr liegen - sie muss nur um die Bäume herumlaufen.
# Glücklicherweise stehen diese immer einzeln. Schreibe ein Programm, das sie bis zur Erdbeere führt!

