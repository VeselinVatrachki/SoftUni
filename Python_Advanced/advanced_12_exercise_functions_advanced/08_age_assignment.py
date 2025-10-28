def age_assignment(*args, **kwargs):
    persons = {}
    # to try to fill persons{} with dict comprehensions
    for name in args:
        persons[name] = kwargs[name[0]]

    result = []
    persons = sorted(persons.items())

    for name, age in persons:
        result.append(f"{name} is {age} years old.")

    return "\n".join(result)




#TEST CODE
print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
