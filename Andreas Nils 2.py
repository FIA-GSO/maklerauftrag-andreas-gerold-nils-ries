print("Bitte füllen Sie den Kopf aus")
print("Wie lautet der Maklername:")
name = input();
print (" Wie heißt die Wohnung, welche Sie gerade besichtigen?")
objekt = input();
print("Welchen Tag ist heute?")
datum = input();

print("Wie viele Räume hat die Wohnung?")
gesamt_rooms = 0

rooms_1 = int(input())
for i in range (rooms_1):
    print("Handelt es sich um einen komplexen Raum? Antworten Sie mit 'Ja' oder 'Nein'")
    raum_1 = input();
    if raum_1 ==  "Ja":
        print(" Aus wie vielen Vierecken besteht der Raum?")
        anzahl_viereck = int(input());
        gesamt_vierecke = 0
        for i in range (anzahl_viereck):
            print("Geben Sie die Länge des Vierecks an")
            Laenge = int(input());
            print("Geben Sie die Breite des Vierecks an")
            Breite = int(input());
            gesamt_vierecke = gesamt_vierecke + Laenge*Breite
            print(f"Gesamtfläche",{gesamt_vierecke},"m^2")
            
    else:
        if raum_1 == "Nein":
            print("Geben Sie die Länge des Raumes an")
            Laenge_A2 = int(input());
            print("Geben Sie die Breite des Raumes an")
            Breite_A2 = int(input());
            raum_2 = Laenge_A2 * Breite_A2
            print("Die Größe des Raumes beträgt:" ,raum_2,"m^2")
gesamt_rooms = gesamt_vierecke + raum_2
durchschnitt = gesamt_rooms/rooms_1
print(f"Gesamtfläche der Wohnung", {gesamt_rooms},"m^2")
print("Die durchschnittliche Fläche pro Raum betragt:",durchschnitt,"m^2")
        
