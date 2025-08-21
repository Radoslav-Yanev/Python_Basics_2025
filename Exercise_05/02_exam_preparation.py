bad_grades_max = int(input())

bad_grade_count = 0
grade_sum = 0
example_count = 0
last_task = ""

while True:
    example_name = input()

    if example_name == "Enough":
        average_grade = grade_sum / example_count
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {example_count}")
        print(f"Last problem: {last_task}")
        break

    grade = int(input())
    grade_sum += grade
    example_count += 1
    last_task = example_name

    if grade <= 4:
        bad_grade_count += 1
        if bad_grade_count >= bad_grades_max:
            print(f"You need a break, {bad_grade_count} poor grades.")
            break