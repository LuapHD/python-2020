from Taschenrechner import Taschenrechner

t = Taschenrechner()

print (t.get_value())

r = input ('Gib hier die erste Zahl ein: ')

r = int(r)

print (t.set_value(r))

while 1 == 1:
    oper = input('Gib deinen Rechenoperator an (+, -, *, / oder %) oder Quit (q): ')

    if oper == 'q':
        quit('Ok')

    z = input('Gib die zweite Zahl an: ')

    z = int(z)

    if oper == '+':
        print(t.add(z))

    elif oper == '-':
        print(t.sub(z))

    elif oper == '*':
        print(t.mult(z))

    elif oper == '/':
        print(t.div(z))

    elif oper == '%':
        print(t.mod(z))



print (t.get_value())