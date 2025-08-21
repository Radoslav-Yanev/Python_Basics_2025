judges = int(input())

total_grades_sum = 0
total_grade_count = 0
result = ""

while True:
    presentation = input()

    if presentation == "Finish":
        break

    current_grades_sum = 0
    for _ in range(judges):
        grade = float(input())
        current_grades_sum += grade

    result += f"{presentation} - {current_grades_sum / judges:.2f}.\n"
    total_grades_sum += current_grades_sum
    total_grade_count += judges

result += f"Student's final assessment is {total_grades_sum / total_grade_count:.2f}."
print(result)