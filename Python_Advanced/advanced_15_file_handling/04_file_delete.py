import os

path = os.path.join("..", "03_file_writer", "my_first_file.txt")

try:
    os.remove(path)
    print("File deleted successfully")
except FileNotFoundError:
    print("File already deleted!")