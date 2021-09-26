from levels import * # Lade alle Level
TIME_S = 0.5 # Wartezeit zwischen den Schritten

current_level = 11 # aktuelles Level auswählen

exec(open("kara.py").read()) # Startet Kara

# Sensoren: onBerry(), treeFront(), treeLeft(), treeRight(), mushroomFront()
# Aktoren: move(), turnLeft(), turnRight(), putBerry(), removeBerry()

# Kara möchte um ihren Wald im Uhrzeigersinn patrouillieren, um die köstlichen Erdbeeren vor einer Horde Brokkolies zu schützen. Programmiere Kara so, dass sie endlos im Uhrzeigersinn um alle Wälder laufen kann.

turnRight()