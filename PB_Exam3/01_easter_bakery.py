PRICE_PER_1KG_SUGAR_PERCENT = 0.25
PRICE_PER_1EGG_SHELL_PERCENT = 0.10
PRICE_PER_1PACAGE_YEAST_PERCENT = 0.80

flour_price_per_1kg = float(input())
flour_in_kg = float(input())
sugar_in_kg = float(input())
eggs_shells_count = int(input())
yeasts_packages_count = int(input())

sugar_price_per_kg = flour_price_per_1kg - (flour_price_per_1kg * PRICE_PER_1KG_SUGAR_PERCENT)
eggs_shell_price = flour_price_per_1kg + (flour_price_per_1kg * PRICE_PER_1EGG_SHELL_PERCENT)
yeast_package_price = sugar_price_per_kg - (sugar_price_per_kg * PRICE_PER_1PACAGE_YEAST_PERCENT)

total_price = (flour_price_per_1kg * flour_in_kg) + (sugar_in_kg * sugar_price_per_kg) + (eggs_shell_price * eggs_shells_count) + (yeast_package_price *  yeasts_packages_count)

print(f"{total_price:.2f}")