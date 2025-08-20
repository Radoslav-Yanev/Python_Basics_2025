username = input()
password = input()

while True:
    try_password = input()

    if try_password == password:
        print(f"Welcome {username}!")
        break

current_password = password