register = {}

command = input()
while command != 'End':

    company, employees_id = command.split(" -> ")

    if employees_id not in register:
        register[company] = register.get(company, {})
        register[company][employees_id] = employees_id

    command = input()

for company in register:
    print(company)
    for employees_id in register[company]:
        print(f"-- {employees_id}")
