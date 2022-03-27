from cgi import print_form
import dblib
import mysql.connector

def dbZugriffswerte():
    """ Funktion, die die Zugriffsdaten für eine MySQL-Datenbank liefert """
    return "localhost", "root", "", "cpu_monitoring"

def init():
    # Verbindung zur Datenbank aufbauen
    print("Verbindung zur Datenbank aufbauen")
    print("")
    host, user, passwd, db = dbZugriffswerte()
    connection = dblib.dbVerbindungAufbauen(host, user, passwd, db)

    result = dblib.dbAbfrageAnweisung(connection, "SELECT * FROM WERTE");
    # Benutzermenü mit Auswahlmöglichkeiten
    print("Wählen Sie eine Abfrage aus:")
    print("----------------------------")
    print("[1] Komplette Datenbank ausgeben")
    print("[2] Nur CPU Auslastung ausgeben")
    print("[3] Nur RAM Nutzung ausgeben")
    print("[4] MIN, MAX, AVG CPU Auslastung ausgeben")
    print("[5] MIN, MAX, AVG RAM Nutzung ausgeben")

    choice = input("Auswahl: ")

    print("")
    print("")

    if choice == '1':
        # Alle Daten aus der Datenbank ausgeben lassen
        result = dblib.dbAbfrageAnweisung(connection, "SELECT * FROM WERTE")

        print("Nr   \t :\t Zeitpunkt\t         :\t CPU\t:\tRAM\t")
        print("--------------------------------------------------------------------------")
        result = dblib.dbAbfrageAnweisung(connection, "SELECT * FROM werte")
        for zeile in result:  # Ergebnis zeilenweise durchlaufen und ausgeben
            print(str(zeile[0]) + "\t :\t " + str(zeile[1]) + "\t :\t " + str(zeile[2])+ "%" +"\t:\t" + str(zeile[3]) + "%")

    if choice == '2':
        # Nur CPU nutzung ausgeben lassen
        result = dblib.dbAbfrageAnweisung(connection, "SELECT t1_ID, t1_zeit, t1_wert FROM werte")

        print("Nr   \t :\t Zeitpunkt\t         :\t CPU")
        print("------------------------------------------------------------")
        result = dblib.dbAbfrageAnweisung(connection, "SELECT * FROM werte")
        for zeile in result:  # Ergebnis zeilenweise durchlaufen und ausgeben
            print(str(zeile[0]) + "\t :\t " + str(zeile[1]) + "\t :\t " + str(zeile[2])+ "%")

    if choice == '3':
        # Nur Ram nutzung ausgeben lassen
        result = dblib.dbAbfrageAnweisung(connection, "SELECT t1_ID, t1_zeit, ram FROM werte")

        print("Nr   \t :\t Zeitpunkt\t         :\t RAM")
        print("------------------------------------------------------------")
        result = dblib.dbAbfrageAnweisung(connection, "SELECT * FROM werte")
        for zeile in result:  # Ergebnis zeilenweise durchlaufen und ausgeben
            print(str(zeile[0]) + "\t :\t " + str(zeile[1]) + "\t :\t " + str(zeile[2])+ "%")

    if choice == '4':
        # CPU Min, Max, Durchschnitts Nutzung ausgeben lassen
        result = dblib.dbAbfrageAnweisung(connection, "SELECT MIN(t1_wert), MAX(t1_wert), AVG(t1_wert) FROM werte")
        print("Minimum: " + str(result[0][0]))
        print("Maximum: " + str(result[0][1]))
        print("Durchschnitt: " + str(result[0][2]))

    if choice == '5':
        # Ram Min, Max, Durchschnitts Nutzung ausgeben lassen
        result = dblib.dbAbfrageAnweisung(connection, "SELECT MIN(ram), MAX(ram), AVG(ram) FROM werte")
        print("Minimum: " + str(result[0][0]))
        print("Maximum: " + str(result[0][1]))
        print("Durchschnitt: " + str(result[0][2]))


    print("")
    print("")
    print("Daten als CSV exportieren...")
    result = dblib.dbAbfrageAnweisung(connection, "SELECT * FROM werte") # Alle Daten aus der Tabelle auswählen
    export_data_as_csv(result)
    print("Fertig!")

    pass
    # Daten als CSV exportieren 
def export_data_as_csv(data):

    f = open("export.csv", "w")
    f.write("t1_ID,t1_zeit,t1_wert,ram\n")

    for row in data:
        f.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")

    f.close()

init()