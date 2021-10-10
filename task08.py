from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 8 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Schreibe ein Programm, das Kara bis zu ihrem Freund dem Baum führt.
# Liegen auf einem Feld Erdbeeren, soll Kara diese aufnehmen; liegen auf einem Feld keine Erdbeeren, soll sie welche ablegen.
# Bei dem Baum angekommen, ist Kara fertig.

turnRight()