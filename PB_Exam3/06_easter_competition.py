import sys

easter_bread_count = int(input())

max_baker_name = ""
max_points = - sys.maxsize

for _ in range(easter_bread_count):
    baker_name = input()

    total_points = 0

    while True:
        command = input()

        if command == "Stop":
            print(f"{baker_name} has {total_points} points.")
            if total_points > max_points:
                max_points = total_points
                max_baker_name = baker_name
                print(f"{max_baker_name} is the new number 1!")
            break

        current_evaluation = int(command)
        total_points += current_evaluation

print(f"{max_baker_name} won competition with {max_points} points!")
