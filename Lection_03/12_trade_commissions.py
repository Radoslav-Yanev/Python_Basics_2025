town = input()
sales = float(input())
commission = -1.1

if town == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05
    elif 500 <= sales <= 1000:
        commission = 0.07
    elif 1000 <= sales <= 10000:
        commission = 0.08
    elif sales > 10000:
        commission = 0.12
elif town == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045
    elif 500 <= sales <= 1000:
        commission = 0.075
    elif 1000 <= sales <= 10000:
        commission = 0.10
    elif sales > 10000:
        commission = 0.13
elif town == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055
    elif 500 <= sales <= 1000:
        commission = 0.08
    elif 1000 <= sales <= 10000:
        commission = 0.12
    elif sales > 10000:
        commission = 0.145

if commission >= 0:
    total = commission * sales
    print(f"{total:.2f}")
else:
    print("error")