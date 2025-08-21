students_ticket_sum = 0
standard_ticket_sum = 0
kid_ticket_sum = 0
result = ""

while True:
    film_name = input()

    if film_name == "Finish":
        break

    capacity = int(input())
    sold_tickets = 0

    while sold_tickets < capacity:
        ticket_type = input()

        if ticket_type == "End":
            break

        if ticket_type == "student":
            students_ticket_sum += 1

        elif ticket_type == "standard":
            standard_ticket_sum += 1

        elif ticket_type == "kid":
            kid_ticket_sum += 1

        sold_tickets += 1

    result += f"{film_name} - {(sold_tickets / capacity) * 100:.2f}% full.\n"

total_tickets = students_ticket_sum + standard_ticket_sum + kid_ticket_sum

result += f"Total tickets: {total_tickets}\n"
result += f"{(students_ticket_sum / total_tickets) * 100:.2f}% student tickets.\n"
result += f"{(standard_ticket_sum / total_tickets) * 100:.2f}% standard tickets.\n"
result += f"{(kid_ticket_sum / total_tickets) * 100:.2f}% kids tickets.\n"

print(result)