country = input().split(", ")
capital = input().split(", ")

result = {country: capital for country, capital in zip(country, capital)}
for country, capital in result.items():
    print(f"{country} -> {capital}")
