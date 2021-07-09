##  Lese alle python Dateien in src Verzeichnis:
##  - print(anzahl_zeilen)
##  - Erzeuge nur eine Datei aus allen vorhandenen Dateien
##  - print(anzahl_buchstabe_c)
##  - Implementiere eine Class copy, die Datei a nach Datei b kopiert

import os

path = 'C:/Users/Paul Kostial/PycharmProjects/Aufgabe18/'
lst = os.listdir(path)
##print(lst)

target = 'AllFiles.txt'
filePathTarget = path + target

i = 0
anzahlC = 0                                                  ##  Das ist der Zähler für die Gesamtzahl c-Buchstaben

for item in lst:

    if item != '.idea' and item != 'venv':

        filePath = path + item

        with open(filePath, 'r') as reader, open(filePathTarget, "a+") as writer:

             ## Alle Zeilen um die Zeilenlängen zu bestimmen
            inhalt = reader.readlines()

            ## Zeilenlänge
            print("File " + item + " ist " +  str(len(inhalt)) + " Zeilen lang")
            i += len(inhalt)

            ## Inhalt kopieren

            writer.writelines(reversed(inhalt))

        with open(filePath, 'r') as reader:                 ## Hier wird das File neu geöffnet, um die Zeilen Einzeln zum Zählen der "c"s zu loopen

            ## c-Zeichen
            line = reader.readline()                        ## Hier wird die erste Zeile gelesen
            fileAnzahlC = 0                                 ##  Das ist der Zähler für die c-Buchstaben im File

            while line != '':                               ## Das ist ein Loop über Zeilen
                for char in line:                           ## Das ist ein Loop über alle Zeichen der Zeile
                    if char == 'c':                         ## Hier wird nach den (kleinen) "c"s gesucht
                        fileAnzahlC += 1
                        anzahlC += 1

                line = reader.readline()                    ## Hier wird die nächste Zeile gelesen

            print("File " + item + " hat " + str(fileAnzahlC) + " c-Zeichen")

print("Alle Files zusammen sind " + str(i) + ' Zeilen lang.')
print("Alle Files zusammen haben " + str(anzahlC) + " c-Zeichen")
