class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

SPECIAL_CHARACTERS = ("@", "*", "&", "%")

while True:
    user_input = input()
    if user_input == 'Done':
        break

    if len(user_input) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if user_input.isdigit() or user_input.isalpha() or all(char in SPECIAL_CHARACTERS for char in user_input):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(char in SPECIAL_CHARACTERS for char in user_input):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in user_input:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")


#TEST CODE
# 1234qwer@
# Done
#
# Qazxwj21
# Done
#
# Password
# Done
