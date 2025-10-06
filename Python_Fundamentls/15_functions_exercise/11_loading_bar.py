def loading_bar(some_number) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loading_percent_as_digit = some_number // 10
    return f"{some_number}% [{'%'*loading_percent_as_digit}{'.'*(10-loading_percent_as_digit)}]\nStill loading..."


number = int(input())
print(loading_bar(number))
