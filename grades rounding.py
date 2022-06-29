def gradingStudents(grades):
    multiple_of_five = 0
    difference = 0
    for i in range(len(grades)):

        if grades[i] < 40:
            continue

        for x in range(grades[i], 101):
            if x % 5 == 0:
                multiple_of_five = x
                break

        difference = abs(grades[i] - multiple_of_five)

        if difference < 3:
            grades[i] = multiple_of_five

        else:
            continue

    return grades


if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)