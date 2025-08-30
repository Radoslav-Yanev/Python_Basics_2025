company_name = input()
adult_ticket_count = int(input())
kid_ticket_count = int(input())
adult_ticket_price = float(input())
tax = float(input())

kid_ticket_price = adult_ticket_price * 0.30
total_ticket_count = adult_ticket_count + kid_ticket_count
total_price = (adult_ticket_count * adult_ticket_price) + (kid_ticket_count * kid_ticket_price) + (total_ticket_count * tax)
agency_income = total_price * 0.20

print(f"The profit of your agency from {company_name} tickets is {agency_income:.2f} lv.")