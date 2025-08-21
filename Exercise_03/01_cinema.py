projection = input()
rows = int(input())
columns = int(input())
price = 0.0

total_capacity = rows * columns

if projection == "Premiere":
    price = 12.00
elif projection == "Normal":
    price = 7.50
elif projection == "Discount":
    price = 5.00

total_price = total_capacity * price

print(f"{total_price:.2f} leva")