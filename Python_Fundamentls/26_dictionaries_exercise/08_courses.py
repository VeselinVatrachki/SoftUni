classes = {}
command = input()

while command != "end":

    course, name = command.split(" : ")

    classes[course] = classes.get(course, {})
    classes[course][name] = name

    command = input()

for course in classes:
    print(f"{course}: {len(classes[course])}")
    for name in classes[course].values():
        print(f"-- {name}")
