print("Which word best describes you?")
print("1. Brave")
print("2. Creative")
print("3. Studious")
print("4. Evil")

q1 = input("Make you selection (1-4): ")

print("What is your favorite creature?")
print("1. Hippogriff")
print("2. Phoenix")
print("3. Rat")
print("4. Cat")

q2 = input("Make you selection (1-4): ")

print("What is your favorite spell?")
print("1. Lumus")
print("2. Winguardium Liviousa")

q3 = input("Make you selection (1-2): ")

if q1 == "1":
    # Griffindor
    if q2 == "3":
        print("Ron Weasly")
    else:
        print("Harry Potter")
elif q1 == "2":
    # Ravenclaw
    print("Luna Lovegood")
elif q1 == "3":
    # Hufflepuff
    print("Cedrick Diggory")
elif q1 == "4":
    # Slytherin
    if q3 == "1":
        print("Severus Snape")
    else:
        print("Draco Malfoy")
else:
    print("Invalid selection")