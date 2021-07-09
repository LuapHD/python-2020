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

    elif (oper == "sum"):
        num3 = input("Gib die dritte Zahl ein: ")
        num4 = input("Gib die vierte Zahl ein: ")
        num5 = input("Gib die fünfte Zahl ein: ")
        num6 = input("Gib die sechste Zahl ein: ")
        num7 = input("Gib die siebte Zahl ein: ")
        num8 = input("Gib die achte Zahl ein: ")
        num9 = input("Gib die neunte Zahl ein: ")
        num10 = input("Gib die zehnte Zahl ein: ")
        num11 = input("Gib die elfte Zahl ein: ")
        num12 = input("Gib die zwölfte Zahl ein: ")
        num13 = input("Gib die dreizehnte Zahl ein: ")

        num3 = int(num3)
        num4 = int(num4)
        num5 = int(num5)
        num6 = int(num6)
        num7 = int(num7)
        num8 = int(num8)
        num9 = int(num9)
        num10 = int(num10)
        num11 = int(num11)
        num12 = int(num12)
        num13 = int(num13)

        print (sum((num1, num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13)))

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
