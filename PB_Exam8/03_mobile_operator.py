contract_term = input()
contract_type = input()
internet = input()
months = int(input())

price = {
    "one": {
        "Small": 9.98,
        "Middle": 18.99,
        "Large": 25.98,
        "ExtraLarge": 35.99
    },
    "two": {
        "Small": 8.58,
        "Middle": 17.09,
        "Large": 23.59,
        "ExtraLarge": 31.79
    }
}

monthly_price = price[contract_term][contract_type]

if internet == "yes":
    if monthly_price <= 10:
        monthly_price += 5.50

    elif monthly_price <= 30:
        monthly_price += 4.35

    else:
        monthly_price += 3.85

if contract_term == "two":
    monthly_price -= monthly_price * 0.0375

total_price = monthly_price * months

print(f"{total_price:.2f} lv.")



