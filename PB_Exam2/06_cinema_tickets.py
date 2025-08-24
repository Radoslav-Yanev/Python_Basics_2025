student_tickets_count = 0
standard_ticket_count = 0
kids_tickets_count = 0
total_tickets = 0

while True:
    film_name = input()

    if film_name == "Finish":
        break

    free_seats = int(input())
    sold_ticket_count = 0

    while sold_ticket_count < free_seats:
        ticket_type = input()

        if ticket_type == "End":
            break

        if ticket_type == "student":
            student_tickets_count += 1

        elif ticket_type == "standard":
            standard_ticket_count += 1

        elif ticket_type == "kid":
            kids_tickets_count += 1

        sold_ticket_count += 1
        total_tickets += 1

    full_percentage = (sold_ticket_count / free_seats) * 100
    print(f"{film_name} - {full_percentage:.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets_count / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_ticket_count / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kids_tickets_count / total_tickets) * 100:.2f}% kids tickets.")
