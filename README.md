# Python Taschenrechner GUI

## Beschreibung

Dieses Projekt ist ein einfacher Taschenrechner mit einer grafischen Benutzeroberfläche (GUI), der mit Python erstellt wurde. Er ermöglicht grundlegende Rechenoperationen wie Addition, Subtraktion, Multiplikation und Division.

## Funktionen

* Einfache und benutzerfreundliche GUI.
* Grundlegende Rechenoperationen (+, -, \*, /).
* Fehlerbehandlung für ungültige Eingaben (z. B. Buchstaben anstelle von Zahlen).
* Fehlerbehandlung für die Division durch Null.
* Einbindung eines Hintergrundbildes.

## Installation

1.  Stelle sicher, dass Python und pip installiert sind.
2.  Klone das Repository: `git clone http://www.linguee.de/englisch-deutsch/uebersetzung/des+repositories.html`
3.  Navigiere zum Projektverzeichnis: `cd taschenrechner-gui`
4.  Installiere die erforderlichen Bibliotheken: `pip install Pillow`
5.  Führe das Skript aus: `python taschenrechner_gui.py`

## Verwendung

1.  Starte das Programm.
2.  Gib die Zahlen in die Eingabefelder ein.
3.  Klicke auf die gewünschte Rechenoperation.
4.  Das Ergebnis wird angezeigt.

## EXE-Erstellung

1.  Installiere PyInstaller: `pip install pyinstaller`
2.  Navigiere zum Projektverzeichnis.
3.  Führe den folgenden Befehl aus: `pyinstaller --onefile --windowed taschenrechner_gui.py`
4.  Die EXE-Datei befindet sich im Ordner `dist`.

## Zusätzliche Hinweise

* Das Hintergrundbild (`hintergrund.jpg`) muss sich im selben Verzeichnis wie das Python-Skript befinden.
* Die Größe des Hintergrundbildes kann angepasst werden.

## Autor

* \[Dennis Garscha]

## Lizenz

Dieses Projekt ist unter der \[Lizenz, z. B. MIT-Lizenz] lizenziert.

## Danksagungen

* Tkinter-Dokumentation
* PIL (Pillow)-Dokumentation
* Stack Overflow (und andere Online-Ressourcen)
