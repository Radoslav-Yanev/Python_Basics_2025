film_name = input()
days_count = int(input())
tickets_count = int(input())
ticket_price = float(input())
cinema_percentage = int(input()) / 100

total_price = (ticket_price * tickets_count) * days_count
cinema_money = total_price * cinema_percentage
studio_revenue = total_price - cinema_money

print(f"The profit from the movie {film_name} is {studio_revenue:.2f} lv.")

