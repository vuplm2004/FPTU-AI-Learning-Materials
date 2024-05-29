def read_data(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            SBD, name, maths, literature, english = line.strip().split(',')
            students.append({
                'SBD': SBD,
                'name': name,
                'maths': int(maths),
                'literature': int(literature),
                'english': int(english)
            })
    return students

def display_info(SBD, students):
    for student in students:
        if student['SBD'] == SBD:
            print("Registration Number:", student['SBD'])
            print("Full Name:", student['name'])
            print("Math Score:", student['maths'])
            print("Literature Score:", student['literature'])
            print("English Score:", student['english'])
            return
    print("Student not found.")


def get_passed_students(passed_score, students):
    successful_students = []
    for student in students:
        maths = student['maths']
        literature = student['literature']
        english = student['english']

        if maths == 1 or literature == 1 or english == 1:
            continue

        total_score = (maths * 2) + (literature * 2) + english
        if total_score >= passed_score:
            successful_students.append(student)

    return successful_students


def main():
    filename = input("Enter filename: ")
    students = read_data(filename)

    while True:
        print("1. Display Student Information")
        print("2. Get List of Passed Students")
        print("3. Exit")

        choice = input("Enter 1-3: ")

        if choice == '1':
            SBD = input("Enter SBD: ")
            display_student_info(SBD, students)

        elif choice == '2':
            passed_score = int(input("Enter the number of passed score: "))
            passed_students = get_passed_students(passed_score, students)

            print("\nPassed Students:")
            for student in passed_students:
                print("SBD:", student['SBD'])
                print("Full Name:", student['name'])

        elif choice == '3':
            print("Exit")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
