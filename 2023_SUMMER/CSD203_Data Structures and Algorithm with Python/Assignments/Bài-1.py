class Data:
    def __init__(self, studentID, studentName, studentGrade):
        self.studentID = studentID
        self.studentName = studentName
        self.studentGrade = studentGrade

class studentInfo:
    #create a temp list:
    def __init__(self):
        self.students = []
    #create studet record and save in file data.txt:
    def addStudent(self, student):
        self.students.append(student)
        
        with open("data.txt", "a") as f:
            f.write(f"Student ID: {student.studentID}\nStudent Name: {student.studentName}\nGrade: {student.studentGrade}\n")
    #search student info from the list:   
    def searchStudent(self, studentID):
        for student in self.students:
            if student.studentID == studentID:
                print(f"Student ID: {student.studentID}\nStudent Name: {student.studentName}\nGrade: {student.studentGrade}\n")
                return

        print("Not Found")
    #display studnet info in the list:
    def displayInfo(self):
        for student in self.students:
            print(f"Student ID: {student.studentID}\nStudent Name: {student.studentName}\nGrade: {student.studentGrade}\n")
    
def main():
    organizer = studentInfo()
    
    while True:
        print("Main Menu")
        print("1. Create student record")
        print("2. Search studnet record")
        print("3. Display studnet record")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            while True:
                studentID = input("Enter student ID: ")
                studentName = input("Enter student name: ")
                studentGrade = input("Enter student grade: ")
                
                student = Data(studentID, studentName, studentGrade)
                organizer.addStudent(student)
                
                continueEnter = input("Do you want to continue enter information? (Y/N) ")
                #asking user to choose whether or not they want to continue:
                if continueEnter.lower() != "y":
                    break
        elif choice == "2":
            studentID = input("Enter student ID: ")
            organizer.searchStudent(studentID)
        elif choice == "3":
            organizer.displayInfo()
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
