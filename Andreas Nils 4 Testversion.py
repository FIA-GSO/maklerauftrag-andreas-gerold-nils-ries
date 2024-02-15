print("Bitte füllen Sie den Kopf aus")
print("Mitarbeitername:")
name = input();
print("Wohnungsname:")
objekt = input();
print("Datum:")
datum = input();

print("Anzahl der Räumlichkeiten:")
gesamt0 = 0
gesamt1 = 0
gesamt2 = 0
rooms = int(input());
for i in range (rooms):
    gesamt4 = 0
    gesamt5 = 0
    print("Ist der Raum komplex? 'ja','nein'")
    raum0 = input();
    if raum0 == "ja":
        print("Anzahl der Vierecke:")
        vierecke = int(input());
        for i in range (vierecke):
            print("Länge:")
            länge = int(input());
            print("Breite:")
            breite = int(input());
            gesamt1 = gesamt1 + (länge * breite)
            gesamt4 = gesamt4 + (länge * breite)
            print(f"Gesamtfläche:", {gesamt4},"m^2")
    else:
        if raum0 == "nein":
            print("Länge:")
            länge1 = int(input());
            print("Breite:")
            breite1 = int(input());
            gesamt0 = gesamt0 + (länge1 * breite1)
            gesamt5 = länge1 * breite1
            print(f"Gesamtfläche:",{gesamt5},"m^2")
gesamt2 = gesamt1 + gesamt0
durchschnitt = gesamt2/rooms
print(f"Gesamtfläche der Wohnung", {gesamt2},"m^2")
print("Die durchschnittliche Fläche pro Raum betragt:",durchschnitt,"m^2")
        
        
