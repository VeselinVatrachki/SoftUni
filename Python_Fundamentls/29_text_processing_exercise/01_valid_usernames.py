# def length_of_username(username):
#     if 3 <= len(username) <= 16:
#         return True
#     return False
#
#
# def contains_of_username(username):
#     for letter in username:
#         if not (letter.isalnum() or letter == "-" or letter == "_"):
#             return False
#     return True
#
#
# def no_redundant_symbols(username):
#     if " " not in username:
#         return True
#     return False
#
#
# def valid_username(username):
#     if length_of_username(username) and \
#         contains_of_username(username) and \
#         no_redundant_symbols(username):
#         return True
#     return False
#
# usernames = input().split(", ")
# for username in usernames:
#     if valid_username(username):
#         print(username)

def length_of_username(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def contains_of_username(username):
    for letter in username:
        if not (letter.isalnum() or letter == "-" or letter == "_"):
            return False
    return True


def no_redundant_symbols(username):
    if " " not in username:
        return True
    return False


def valid_username(username):
    if length_of_username(username) and \
        contains_of_username(username) and \
        no_redundant_symbols(username):
        return username


usernames = input().split(", ")
for username in usernames:
    if valid_username(username):
        print(valid_username(username))
