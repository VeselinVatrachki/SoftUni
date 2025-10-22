phones = input().split(", ")
command = input()


def add_phone(phone):
    if phone not in phones:
        phones.append(phone)


def remove_phone(phone):
    if phone in phones:
        phones.remove(phone)


def bonus_phone(old_phone, new_phone):
    if old_phone in phones:
        phones.insert(phones.index(old_phone) + 1, new_phone)


def last_phone(phone):
    if phone in phones:
        phones.remove(phone)
        phones.append(phone)


while command != "End":
    command = command.split(" - ")
    type_of_command = command[0]
    phone = command[1]
    if type_of_command == "Add":
        add_phone(phone)
    elif type_of_command == "Remove":
        remove_phone(phone)
    elif type_of_command == "Bonus phone":
            old_phone = phone.split(":")[0]
            new_phone = phone.split(":")[1]
            bonus_phone(old_phone, new_phone)
    elif type_of_command == "Last":
        last_phone(phone)

    command = input()

result = ", ".join(phones)
print(result)
