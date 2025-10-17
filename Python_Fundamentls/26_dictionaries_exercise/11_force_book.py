# command = input()
# force_power = {}
#
# while command != "Lumpawaroo":
#
#     if "|" in command:
#         force_side, force_user = command.split(" | ")
#         force_user_is_part_of_the_force = False
#
#         for list_of_force_users in force_power.values():
#             if force_user in list_of_force_users:
#                 force_user_is_part_of_the_force = True
#                 break
#         if not force_user_is_part_of_the_force:
#             if force_side not in force_power.keys():
#                 force_power[force_side] = []
#             force_power[force_side].append(force_user)
#
#     elif "->" in command:
#         force_user, force_side = command.split(" -> ")
#
#         for list_of_force_users in force_power.values():
#             if force_user in list_of_force_users:
#                 list_of_force_users.remove(force_user)
#                 break
#         if force_side not in force_power.keys():
#             force_power[force_side] = []
#         force_power[force_side].append(force_user)
#         print(f"{force_user} joins the {force_side} side!")
#
#     command = input()
#
# for force_side, list_of_force_users in force_power.items():
#     if list_of_force_users:
#         print(f"Side: {force_side}, Members: {len(list_of_force_users)}")
#         for force_user in list_of_force_users:
#             print(f"! {force_user}")


force_power = {}

command = input()
def add_user_to_side(force_name, force_side):
    for force_users in force_power.values():
        if force_name in force_users:
            return
    force_power[force_side] = force_power.get(force_side, []) + [force_name]


def change_side(force_name, force_side):
    for sides, names in force_power.items():
        if force_name in names:
            force_power[sides].remove(force_name)
            break
    force_power[force_side] = force_power.get(force_side, []) + [force_name]
    print(f"{force_name} joins the {force_side} side!")


while command != "Lumpawaroo":

    if "|" in command:
        force_side, force_name = command.split(" | ")
        add_user_to_side(force_name, force_side)

    elif "->" in command:
        force_side, force_name = command.split(" -> ")
        change_side(force_name, force_side)

    command = input()

for force_sides, force_names in force_power.items():
    if force_names:
        print(f"Side: {force_sides}, Members: {len(force_names)}")
        for force_name in force_names:
            print(f"! {force_name}")
