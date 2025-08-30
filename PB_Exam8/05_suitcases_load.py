capacity = float(input())

bag_count = 0
free_space = capacity

while True:
    command = input()

    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    current_bag_value = float(command)
    bag_count += 1

    if bag_count % 3 == 0:
        current_bag_value += current_bag_value * 0.10

    if current_bag_value > free_space:
        print("No more space!")
        bag_count -= 1
        break

    free_space -= current_bag_value

print(f"Statistic: {bag_count} suitcases loaded.")

