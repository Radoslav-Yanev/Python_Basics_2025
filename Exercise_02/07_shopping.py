VIDEO_CARD_PRICE = 250
DISCOUNT = 0

peter_budget = float(input())
video_card_count = int(input())
processors_count = int(input())

ram_count = int(input())
total_video_car_price = video_card_count * VIDEO_CARD_PRICE
processor_price = total_video_car_price * 0.35
ram_price = total_video_car_price * 0.10


total_processor_price = processors_count * processor_price
total_ram_price = ram_count * ram_price

materials_price = total_video_car_price + total_processor_price + total_ram_price

if video_card_count > processors_count:
    DISCOUNT += materials_price * 0.15

total_price = materials_price - DISCOUNT

if peter_budget >= total_price:
    print(f"You have {peter_budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - peter_budget:.2f} leva more!")