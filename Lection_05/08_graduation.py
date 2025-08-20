student_name = input()

excluded_count = 0
grade = 1
evaluation_sum = 0

while True:
    current_evaluation = float(input())

    if current_evaluation < 4.00:
        excluded_count += 1
        if excluded_count > 1:
            print(f"{student_name} has been excluded at {grade} grade")
            break
        continue

    evaluation_sum += current_evaluation

    if grade == 12:
        average_evaluation = evaluation_sum / 12
        print(f"{student_name} graduated. Average grade: {average_evaluation:.2f}")
        break
    grade += 1