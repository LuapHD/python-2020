first_number = 10
second_number = 20
print(first_number + second_number)

first_number = 10
second_number = 20
print(first_number - second_number)

first_number = 10
second_number = 20
print(first_number * second_number)

first_number = 10
second_number = 20
print(first_number / second_number)

first_number = 50
second_number = 40
print(first_number % second_number)



print("""
      ====================================================
      ==                 Taschenrechner                 ==
      ====================================================
    """)

num1 = input("Gib die erste Zahl ein: ")
oper = input("Welche Rechenoperation (+,-,*,/) soll durchgeführt werden? ")
num2 = input("Gib die zweite Zahl ein: ")

num1 = int(num1)
num2 = int(num2)

if (oper == "+"):
    print (num1 + num2)

elif (oper == "-"):
    print (num1 - num2)

elif (oper == "*"):
    print (num1 * num2)

elif (oper == "/"):
    print (num1 / num2)

else:
    print ("Keine richtige Angabe")