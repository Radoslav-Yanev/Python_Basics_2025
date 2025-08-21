first_number = int(input())
second_number = int(input())
operator = input()

result = 0

if operator == "+":
    result = (f"{first_number} {operator} {second_number} = {first_number + second_number}"
              f"{' - even' if (first_number + second_number) % 2 == 0 else ' - odd'}")

elif operator == "-":
    result = (f"{first_number} {operator} {second_number} = {first_number - second_number}"
              f"{' - even' if (first_number - second_number) % 2 == 0 else ' - odd'}")
elif operator == "*":
    result = (f"{first_number} {operator} {second_number} = {first_number * second_number}"
              f"{' - even' if (first_number * second_number) % 2 == 0 else ' - odd'}")

elif second_number == 0:
    result = f"Cannot divide {first_number} by zero"

elif operator == "/":
    result = f"{first_number} {operator} {second_number} = {first_number / second_number:.2f}"

elif operator == "%":
    result = f"{first_number} {operator} {second_number} = {first_number % second_number}"

print(result)