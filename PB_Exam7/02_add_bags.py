luggage_above_20kg_tax = float(input())
luggage_kg = float(input())
day_to_fly = int(input())
luggage_count = int(input())

tax = 0

if luggage_kg > 20:
    tax = luggage_above_20kg_tax

elif 10 < luggage_kg <= 20:
    tax = luggage_above_20kg_tax * 0.50

else:
    tax = luggage_above_20kg_tax * 0.20

if day_to_fly > 30:
    tax += tax * 0.10

elif 7 <= day_to_fly <= 30:
   tax += tax * 0.15

else:
    tax += tax * 0.40

total_price = tax * luggage_count

print(f"The total price of bags is: {total_price:.2f} lv.")


