from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 4 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()
# Ausgabe: print("Ausgabe")

# Prüfe, ob Kara auf einer Erdbeere sitzt. Ist das der Fall, soll sie einen Jubelschrei ausstoßen.
# Wenn sie auf keiner Erdbeere sitzt, soll sie deprimiert ausstoßen, dass sie schon ihr ganzes Leben viel Pech hat.

