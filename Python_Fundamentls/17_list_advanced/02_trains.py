# wagons = [0] * int(input())
#
# while True:
#     command = input().split()
#
#     if command[0] == "End":
#         print(wagons)
#         break
#
#     elif command[0] == "add":
#         number_of_people = int(command[1])
#         wagons[-1] += number_of_people
#
#     elif command[0] == "insert":
#         index = int(command[1])
#         people = int(command[2])
#         wagons[index] += people
#
#     elif command[0] == "leave":
#         index = int(command[1])
#         people = int(command[2])
#         wagons[index] -= people
#
#
class Train:
    def __init__(self, number_of_wagons):
        self.train = [0] * number_of_wagons

    def add(self, people):
        self.train[-1] += people

    def insert(self, index, people):
        self.train[index] += people

    def leave(self, index, people):
        self.train[index] -= people

    def __str__(self):
        return str(self.train)


def main_func():
    number_of_wagons = int(input())
    train = Train(number_of_wagons)

    while True:
        command = input()

        if command == 'End':
            break

        command_parts = command.split()
        current_action = command_parts[0]

        if current_action == 'add':
            people = int(command_parts[1])
            train.add(people)

        elif current_action == 'insert':
            index = int(command_parts[1])
            people = int(command_parts[2])
            train.insert(index, people)

        elif current_action == 'leave':
            index = int(command_parts[1])
            people = int(command_parts[2])
            train.leave(index, people)

    print(train)


main_func()
