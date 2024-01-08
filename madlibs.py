"""
Mutiple ways to do string concatenation
name = stef
print("Hi my name " + name)
print("Hi my name is {}".format(name))
print(f"Hi my name is {name}")
"""
adj = input('Adjective: ')
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")
madlib = f"Computer programming is so {adj}! It makes me so excitied all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)