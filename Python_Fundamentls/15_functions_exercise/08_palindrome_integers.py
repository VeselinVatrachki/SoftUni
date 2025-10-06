def is_palindrome(number_as_string):
    return number_as_string[::-1] == number_as_string


numbers_as_string = input().split(", ")
for number in numbers_as_string:
    print(is_palindrome(number))
