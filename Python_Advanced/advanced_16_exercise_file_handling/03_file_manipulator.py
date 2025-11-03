import os


while True:
    command = input()
    if command == "End":
        break

    cmd, file_name, *args = command.split("-")

    if cmd == "Create":
        open(file_name, "w").close()

    elif cmd == "Add":
        with open(file_name, "a") as file:
            file.write(f"{args[0]}\n")

    elif cmd == "Replace":
        try:
            with open(file_name, "r+") as file:
                content = file.read()
                file.seek(0)
                file.truncate(0)
                file.write(content.replace(args[0], args[1]))
        except FileNotFoundError:
            print("An error occurred")

    elif cmd == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")