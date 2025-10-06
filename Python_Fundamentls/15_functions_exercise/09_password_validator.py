def is_valid(some_string: str):
    lst_char = []
    lst_num = []
    lst_symbols = []
    for char in some_string:
        if char.isalpha():
            lst_char.append(char)
        elif char.isnumeric():
            lst_num.append(str(char))
        else:
            lst_symbols.append(str(char))
    password = lst_char + lst_num + lst_symbols
    if 6 <= len(password) <= 10 and len(lst_num) >= 2 and len(lst_symbols) == 0:
        return "Password is valid"
    else:
        if len(lst_symbols) != 0 and len(lst_num) < 2:
            return "Password must consist only of letters and digits\nPassword must have at least 2 digits"
        elif len(lst_symbols) != 0 and len(lst_num) >= 2:
            return "Password must consist only of letters and digits"
        elif not 6 <= len(password) <= 10 and len(lst_num) < 2:
            return "Password must be between 6 and 10 characters\nPassword must have at least 2 digits"
        elif 6 <= len(password) <= 10 and len(lst_num) < 2:
            return "Password must have at least 2 digits"
        elif not 6 <= len(password) <= 10:
            return "Password must be between 6 and 10 characters"


password_string = input()
print(is_valid(password_string))
