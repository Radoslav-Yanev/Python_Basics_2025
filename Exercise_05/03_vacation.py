needed_money = float(input())
balance = float(input())

day_count = 0
spend_day_count = 0
is_money_saved = False

while spend_day_count < 5:
    action_type = input()
    money = float(input())

    day_count += 1

    if action_type == "spend":
        spend_day_count += 1
        balance = balance - money if balance > money else 0

    elif action_type == "save":
        spend_day_count = 0
        balance += money

    if balance >= needed_money:
        is_money_saved = True
        break

if is_money_saved:
    print(f"You saved the money for {day_count} days.")

else:
    print(f"You can't save the money.\n{day_count}")