command = input()
name = ""
while command != "Welcome!":

    if command == "Voldemort":
        print("You must not speak of that name!")
        break

    if len(command) < 5:
        name = command
        print(f"{name} goes to Gryffindor.")
    elif len(command) == 5:
        name = command
        print(f"{name} goes to Slytherin.")
    elif len(command) == 6:
        name = command
        print(f"{name} goes to Ravenclaw.")
    elif len(command) > 6:
        name = command
        print(f"{name} goes to Hufflepuff.")

    command = input()
else:
    print("Welcome to Hogwarts.")
