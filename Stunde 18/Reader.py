#f = open ('Test' , 'r')

#print (f.readline(1))
#print (f.readline(1))
#print (f.readline(1))

#f1 = open ('Test2' , 'w')
#f1.write ('He He')

FilePath= "person.py"
with open(FilePath, 'r') as reader:
    print(reader.read())

filepath= "personTest.py"
with open(filepath, 'r') as reader:
    print(reader.read())

Filepath= "Taschenrechner.py"
with open(Filepath, 'r') as reader:
    print(reader.read())

filePath= "Taschenrechner UnitTest.py"
with open(filePath, 'r') as reader:
    print(reader.read())

print('person.py hat')
print('')

lineNr = 1
with open(FilePath, 'r') as reader:
   line = reader.readline()
   while line != '':
      print(str(lineNr) + "\t" + line)
      line = reader.readline()
      lineNr +=1

print('')
print('Zeilen')

print('Taschenrechner UnitTest.py hat')
print('')

lineNr = 1
with open(filePath, 'r') as reader:
   line = reader.readline()
   while line != '':
      print(str(lineNr) + "\t" + line)
      line = reader.readline()
      lineNr +=1

print('')
print('Zeilen')

print('personTest.py hat')
print('')

lineNr = 1
with open(filepath, 'r') as reader:
   line = reader.readline()
   while line != '':
      print(str(lineNr) + "\t" + line)
      line = reader.readline()
      lineNr +=1

print('')
print('Zeilen')


print('Taschenrechner.py hat')
print('')

lineNr = 1
with open(Filepath, 'r') as reader:
   line = reader.readline()
   while line != '':
      print(str(lineNr) + "\t" + line)
      line = reader.readline()
      lineNr +=1
print('')
print('Zeilen')

filePath= 'C:/Users/Paul Kostial/PycharmProjects/Aufgabe18/Test'

msg = "Test"
with open(filePath, 'w') as writer:
    writer.write(msg)

with open(filePath, 'a') as a_writer:
    a_writer.write('')

import os

path = 'C:/Users/Paul Kostial/PycharmProjects/Aufgabe18/'
lst = os.listdir(path)
print(lst)