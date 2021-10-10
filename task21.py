from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 21 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Programmiere Kara so, dass sie eine Kleeblatt-Spirale (bei uns eine Erdbeerspirale) wie die unten dargestellte zeichnet.
# Kara läuft dabei aus deren unteren Ecke los. Jede Seite wird genau 1 Kleeblatt kürzer als die Vorangehende.
# Die erste Linie soll 14 Kleeblätter lang sein.

putBerry()
