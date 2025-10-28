def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheese = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for cheese, quantity in sorted_cheese:
        result += f"{cheese}\n"
        sorted_quantity = sorted(quantity, reverse=True)
        result += "\n".join([str(el) for el in sorted_quantity]) + "\n"

    return result

