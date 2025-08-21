FACEBOOK_PENALTY_PRICE = 150
INSTAGRAM_PENALTY_PRICE = 100
REDDIT_PENALTY_PRICE = 50

open_tabs_count = int(input())
salary = int(input())

is_lost_salary = False

for _ in range(open_tabs_count):
    current_tab = input()

    if current_tab == "Facebook":
        salary -= FACEBOOK_PENALTY_PRICE

    elif current_tab == "Instagram":
        salary -= INSTAGRAM_PENALTY_PRICE

    elif current_tab == "Reddit":
        salary -= REDDIT_PENALTY_PRICE

    if salary <= 0:
        is_lost_salary = True
        break

if is_lost_salary:
    print(f"You have lost your salary.")
else:
    print(salary)