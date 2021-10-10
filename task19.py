from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 19 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Kara zieht fröhlich ihr Frühstücksbrötchen über die Wiese. Läuft Sie nur über Erdbeeren schmeckt es danach sehr gut,
# sonst schmeckt das Brötchen eher nach Schnittlauch. Laufe über alle Erdbeeren.

turnRight()
