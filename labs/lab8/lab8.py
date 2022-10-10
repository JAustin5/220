"""
Name: <Jalena Austin>
<weighted_average>.py

Problem: <Being able to use files and formulating any equations for a file to be read and
    written to another file with the open file's information.>

Certification of Authenticity:
<I certify that this assignment is my own work, but I discussed it with: <Ashely Woods, Isaiah Stapleton>
"""


def weighted_average(in_file_name, out_file_name):
    grade_file = open(in_file_name, 'r')
    grades_file = grade_file.readlines()
    avg_file = open(out_file_name, 'w')
    class_average = 0
    num_students = 0

    for lines in grades_file:
        student_info = lines.split(':')
        grades = student_info[1].split()
        student_weights = grades[0::2]
        student_grade = grades[1::2]
        student_average = 0

        for i in range(len(student_weights)):
            student_average = (eval(student_weights[i]) * eval(student_grade[i])) + student_average
        student_average = student_average / 100

        total_weight = 0
        for j in student_weights:
            total_weight = total_weight + eval(j)

        if total_weight == 100:
            true_weights = (student_info[0] + "'s average: " + str(round(student_average, 1)) + '\n')
            avg_file.write(true_weights)
            class_average += student_average
            num_students += 1

        elif total_weight < 100:
            false_weights = (student_info[0] + "'s average: " + '' +
                             'Error: The weights are less than 100.\n')
            avg_file.write(false_weights)

        else:
            false_2_weights = (student_info[0] + "'s average: " + '' +
                               "Error: The weights are more than 100.\n")
            avg_file.write(false_2_weights)

    final_average = class_average / num_students
    final_average_string = "Class average: " + str(round(final_average, 1))
    avg_file.write(final_average_string)

    grade_file.close()
    avg_file.close()


def main():
    weighted_average("grades.txt", "output.txt")


if __name__ == "__main__":
    main()
