print(sum((1, 2, 3, 4, 5)))

def global_var(x):
    global y
    y = x

global_var(3)
print(y)
## Hier wird der global Variable "y" der Wert von der global Variable "x" (3) gegeben und geprinted


x = 12
i = 0
while i < x:
    print(i)
    i += 1
## Hier werden solange i < x ist i geprinted und um 1 erhöt das passiert zwölf mal und dan ist i= x.


for n in range(1, 11):
    print(n)
## Hier werden dei Zahlen 1 bis 11 geprinted aber einfacher.

def calc_run():

    print("""
          ====================================================
          ==                 Taschenrechner                 ==
          ====================================================
        """)

    num1 = input("Gib die erste Zahl ein: ")
    oper = input("Welche Rechenoperation (+,-,*,/ oder sum) soll durchgeführt werden? ")
    num2 = input("Gib die zweite Zahl ein: ")



    num1 = int(num1)
    num2 = int(num2)

    if (oper == "+"):
        print (num1 + num2)

    if (oper == "sum"):
        sum((num1, num2))

    elif (oper == "-"):
        print (num1 - num2)

    elif (oper == "*"):
        print (num1 * num2)

    elif (oper == "/"):
        print (num1 / num2)

    elif (oper == "sum"):
        print (sum((num1, num2, )))

    else:
        print ("Keine richtige Angabe")
        quit()

calc_run()

