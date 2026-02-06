pokemon = input("Choose a Pokemon")

if pokemon == "Charmander":
    print("Gary chooses Squirtle for the battle")
    print("1) Use Tackle")
    print("2) Use Ember")
    move = input("Select your move")
    if move == "1":
        print("You used Tackle")
    else:
        print("You used Ember (not very effective)")
elif pokemon == "Squirtle":
    print("Gary chooses Bulbasaur for the battle")
    print("1) Use Tackle")
    print("2) Use Bubble")
    move = input("Select your move")
    if move == "1":
        print("You used Tackle")
    else:
        print("You used Bubble (not very effective)")
