product_name = input()
fruit_type = ""

if ((product_name == "banana")
        or (product_name == "apple")
        or (product_name == "kiwi")
        or (product_name == "cherry")
        or (product_name == "lemon")
        or (product_name == "grapes")):
    fruit_type = "fruit"
elif ((product_name == "tomato")
      or (product_name == "cucumber")
      or (product_name == "pepper")
      or (product_name == "carrot")):
    fruit_type = "vegetable"
else:
    fruit_type = "unknown"

print(fruit_type)