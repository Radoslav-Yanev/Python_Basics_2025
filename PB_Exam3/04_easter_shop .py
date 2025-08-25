initial_eggs = int(input())
sold_eggs = 0

while True:
    command = input()

    if command == "Close":
        print(f"Store is closed!\n{sold_eggs} eggs sold.")
        break

    eggs_count = int(input())

    if command == "Buy":
        if eggs_count > initial_eggs:
            print(f"Not enough eggs in store!\nYou can buy only {initial_eggs}.")
            break

        sold_eggs += eggs_count
        initial_eggs -= eggs_count

    elif command == "Fill":
        initial_eggs += eggs_count