# The Mood-Checker

input("Hey! Wie ist Deine Stimmung gerade? Wähle eine der folgenden Optionen: Happy - Traurig - Aufgeregt - Entspannt.")

mymood = input("Meine Stimmung ist: ")

print("Du hast diese Stimmung ausgewählt: " + mymood)

if mymood == "Happy":
    print("YAY!Du bist glücklich!")
elif mymood == "Aufgeregt":
    print("Relax! Du hast keinen Grund zur Aufregung.")
elif mymood == "Traurig":
    print("Oh nein. Kopf hoch!")
elif mymood == "Entspannt":
    print("Cool, bleibt entspannt.")
else:
    print("Sorry, aber dies ist keine gültige Antwort.")

