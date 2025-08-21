numbers_count = int(input())

p1_sum = 0
p2_sum = 0
p3_sum = 0
p4_sum = 0
p5_sum = 0

for _ in range(numbers_count):
    current_number = int(input())

    if current_number < 200:
        p1_sum += 1
    elif 200 <= current_number <= 399:
        p2_sum += 1
    elif 400 <= current_number <= 599:
        p3_sum += 1
    elif 600 <= current_number <= 799:
        p4_sum += 1
    elif current_number >= 800:
        p5_sum += 1

p1_percent = p1_sum / numbers_count * 100
p2_percent = p2_sum / numbers_count * 100
p3_percent = p3_sum / numbers_count * 100
p4_percent = p4_sum / numbers_count * 100
p5_percent = p5_sum / numbers_count * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")