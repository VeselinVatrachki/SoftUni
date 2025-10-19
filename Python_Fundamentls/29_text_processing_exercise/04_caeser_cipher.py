some_string = input()
encrypted_version = ""

for char in some_string:
    encrypt_char = ord(char) + 3
    encrypted_version += chr(encrypt_char)

print(encrypted_version)
