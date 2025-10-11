population = [int(n) for n in input().split(", ")]
minimum_wealth = int(input())

if minimum_wealth > sum(population) / len(population):
    print("No equal distribution possible")

else:
    for num in range(len(population)):
        if population[num] < minimum_wealth:
            result = minimum_wealth - population[num]
            max_number = max(population)
            max_num_index = population.index(max_number)
            number = max_number - result
            population[num] = minimum_wealth
            population[max_num_index] = number
    print(population)

