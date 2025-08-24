hall_rental = int(input())

statues_price = hall_rental - (hall_rental * 0.30)
catering_price = statues_price - (statues_price * 0.15)
sound_price = catering_price / 2

total_sum = statues_price + catering_price + sound_price + hall_rental

print(f"{total_sum:.2f}")