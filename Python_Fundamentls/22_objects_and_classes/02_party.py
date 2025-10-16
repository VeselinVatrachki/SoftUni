class Party:
    def __init__(self):
        self.people = []


party_object = Party()

while True:
    name = input()

    if name == "End":
        break

    party_object.people.append(name)

print(f'Going: {", ".join(party_object.people)}')
print(f"Total: {len(party_object.people)}")
