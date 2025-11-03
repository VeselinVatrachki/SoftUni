try:
    file = open("test.txt")
    print(file.read())
    print("File found")
except FileNotFoundError:
    print("File not found")


#with open("test.txt") as file: