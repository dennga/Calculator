import tkinter as tk  # Importiert die Tkinter-Bibliothek für die GUI

def zahl_drücken(zahl):
    """Fügt eine Zahl zum Eingabefeld hinzu."""
    eingabe.insert(tk.END, zahl)  # Fügt die Zahl am Ende des Eingabefeldes ein

def operator_drücken(operator):
    """Fügt einen Operator zum Eingabefeld hinzu."""
    eingabe.insert(tk.END, operator)  # Fügt den Operator am Ende des Eingabefeldes ein

def berechnen():
    """Berechnet das Ergebnis der eingegebenen Rechenoperation."""
    try:
        ergebnis = eval(eingabe.get())  # Wertet den String im Eingabefeld als Python-Ausdruck aus
        eingabe.delete(0, tk.END)  # Löscht den Inhalt des Eingabefeldes
        eingabe.insert(tk.END, str(ergebnis))  # Fügt das Ergebnis als String in das Eingabefeld ein
    except:
        eingabe.delete(0, tk.END)  # Löscht den Inhalt des Eingabefeldes im Fehlerfall
        eingabe.insert(tk.END, "Fehler")  # Fügt eine Fehlermeldung in das Eingabefeld ein

fenster = tk.Tk()  # Erstellt das Hauptfenster der Anwendung
fenster.title("Calc-U-Later")  # Setzt den Titel des Fensters


eingabe = tk.Entry(fenster, width=20)  # Erstellt ein Eingabefeld mit einer Breite von 20 Zeichen
eingabe.grid(row=0, column=0, columnspan=4)  # Platziert das Eingabefeld in Zeile 0, Spalte 0 und spannt über 4 Spalten

buttons = [  # Definiert die Liste der Buttons
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

reihe = 1  # Initialisiert die Zeilennummer für die Buttons
spalte = 0  # Initialisiert die Spaltennummer für die Buttons

for button in buttons:  # Schleife durch die Liste der Buttons
    if button == "=":  # Wenn der aktuelle Button "=" ist
        tk.Button(fenster, text=button, command=berechnen).grid(row=reihe, column=spalte)  # Erstellt einen Button, der die Berechnungsfunktion aufruft
    elif button in ["+", "-", "*", "/"]:  # Wenn der aktuelle Button ein Operator ist
        tk.Button(fenster, text=button, command=lambda op=button: operator_drücken(op)).grid(row=reihe, column=spalte)  # Erstellt einen Button, der die Operator-Funktion aufruft
    else:  # Wenn der aktuelle Button eine Zahl oder ein Punkt ist
        tk.Button(fenster, text=button, command=lambda z=button: zahl_drücken(z)).grid(row=reihe, column=spalte)  # Erstellt einen Button, der die Zahl-Funktion aufruft
    spalte += 1  # Erhöht die Spaltennummer
    if spalte > 3:  # Wenn die Spaltennummer 4 überschreitet
        spalte = 0  # Setzt die Spaltennummer auf 0 zurück
        reihe += 1  # Erhöht die Zeilennummer

fenster.mainloop()  # Startet die Ereignisschleife der Anwendung