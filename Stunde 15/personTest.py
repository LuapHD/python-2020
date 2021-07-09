from person import Person

alex = Person("alex", 12)
print(alex.toString())
print(alex.get_name())
print(alex.get_age())

alex.set_age(21)
print(alex.get_age())