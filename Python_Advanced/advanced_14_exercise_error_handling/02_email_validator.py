class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass


while True:
    user_input = input()
    if user_input == 'End':
        break

    if "@" not in user_input:
        raise MustContainAtSymbolError("Email must contain @")

    user_name, domain = user_input.split("@")

    if len(user_name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = domain.split(".")
    tags = [".com", ".bg", "org", ".net"]

    if f'.{domain[1]}' not in tags:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")


#TEST CODE
# abc@abv.bg
# peter@gmail.com
# petergmail.com
# peter@gmail.hotmail
