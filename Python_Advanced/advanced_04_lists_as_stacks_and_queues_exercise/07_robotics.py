from collections import deque


robots_data = input().split(";")
robots = []
for robot in robots_data:
    robot_name, process_time = robot.split("-")
    robots.append({"name": robot_name, "process_time": int(process_time), "busy_until_time": 0})

hours, minutes, seconds = [int(x) for x in input().split(":")]
start_time_in_seconds = hours * 3600 + minutes * 60 + seconds

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    curr_product = products.popleft()
    start_time_in_seconds += 1
    is_taken = False

    for robot in robots:
        if robot["busy_until_time"] <= start_time_in_seconds:
            robot["busy_until_time"] = start_time_in_seconds + robot["process_time"]
            h = start_time_in_seconds // 3600
            m = (start_time_in_seconds % 3600) // 60
            s = (start_time_in_seconds % 3600) % 60
            h %= 24
            print(f"{robot['name']} - {curr_product} [{h:02d}:{m:02d}:{s:02d}]")
            is_taken = True
            break

    if not is_taken:
        products.append(curr_product)
