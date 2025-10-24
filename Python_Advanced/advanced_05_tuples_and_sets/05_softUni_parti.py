number_of_guests = int(input())
reservation_code_of_guests = set()

for _ in range(number_of_guests):
    data = input()
    reservation_code_of_guests.add(data)

guests = input()
while guests != "END":
    if guests in reservation_code_of_guests:
        reservation_code_of_guests.remove(guests)
    guests = input()

print(len(reservation_code_of_guests))
for guest in sorted(reservation_code_of_guests):
    print(guest)
