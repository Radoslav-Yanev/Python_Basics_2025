free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

box_count = 0
is_space_left = False

free_space = free_space_width * free_space_length * free_space_height


while free_space > box_count:
    command = input()

    if command == "Done":
        is_space_left = True
        break

    box_count += int(command)

if is_space_left:
    print(f"{free_space - box_count} Cubic meters left.")

else:
    print(f"No more free space! You need {box_count - free_space} Cubic meters more.")