PEN_PACKAGE_PRICE = 5.80
MARKERS_PACKAGE_PRICE = 7.20
DETERGENT_PRICE_FOR_LITER = 1.20

# •	Брой пакети химикали - цяло число в интервала [0...100]
# •	Брой пакети маркери - цяло число в интервала [0...100]
# •	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
# •	Процент намаление - цяло число в интервала [0...100]

pen_package_count = int(input())
markers_package_count = int(input())
detergent_liters_count = int(input())
discount = int(input()) / 100

total_pen_price = pen_package_count * PEN_PACKAGE_PRICE
total_markers_price = markers_package_count * MARKERS_PACKAGE_PRICE
total_detergent_price = detergent_liters_count * DETERGENT_PRICE_FOR_LITER

amount = total_pen_price + total_markers_price + total_detergent_price

total_discount = amount * discount

total_price = amount - total_discount

print(total_price)


