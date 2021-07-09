#Aufgabe 1


fruits = ['apple', 'banana', 'kiwi', 'dragonfruit']
years = [2012,  2013,  2014,  2015]
computer_class = ['Alex', 78, 42, 'Ramin', 98]

print(fruits)
print(years)
print(computer_class)

# Hier wird der Inhalt von Listen definiert (Strings, Intiger und gemischt) und dei Listen werden geprinted


#Aufgabe 2


print(fruits[0])
print(fruits[3])

# Hier wird aus den Listen beschtimmte Elemente geprinted. Die Zahl in den eckigen Klammern gibt die Position in den Listen an (die erste position ist 0) und in den runden Klammern wird die Liste angegeben.

# Achtung Error ! Warum ?
#print(fruits[12])

# Der Code funktioniert nicht weil es in der Liste 'fruits' keine 13te Stelle gibt


#Aufgabe 3


fruits.append('orange')
print(fruits)

# Man kann auch im laufe des Codes noch Listen erweitern


#Aufgabe 4


fruits.remove('dragonfruit')
print(fruits)

# Man kann natürlich auch aus Listen löschen


#Aufgabe 5


for fruit in fruits:
    print('I see  ' + fruit  +  '.')

# Hier wird jedes Element der Liste Fruits nacheinander ausgewählt und in eine Variable übernommen. Dann wird ein Satz erstellt und ausgegeben


#Aufgabe 6


farben = [ 'rot', 'blau', 'gelb', 'grün', 'lila' ]

for farbe in farben:
    print('Ich mag ' + farbe  +  '.')


#Aufgabe 7


student = {'name' : 'Alex', 'old' : 13}
print(student)
print(student['name'])
print(student['old'])

# Update
student.update({'street': 'feuerbach Strasse 12'})
print(student)

student.update({'name': 'Alex2'})
print(student)

# delete an item
del student['street']
print(student)

# Lister von Dictionaries
students = \
[
   {
      "name" : "Alex",
      "age": 12
   },
   {
      "name" : "Andi",
      "age": 43
   }
]

print(students)

print(students[0])

