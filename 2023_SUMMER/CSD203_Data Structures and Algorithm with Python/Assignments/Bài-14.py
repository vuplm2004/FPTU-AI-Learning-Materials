class Student:
    def __init__(self, id: str, name: str, dob: str):
        self.id = id
        self.name = name
        self.dob = dob


class Node:
    def __init__(self, student: Student):
        self.student = student
        self.next = None


class HashTable:
    def __init__(self):
        self.size = 100
        self.table = [None] * self.size
    
    #hash key for given ID
    def hash_key(self, id: str) -> int:
        return int(id) % self.size
    
    #insert a student into the hash table
    def insert(self, student: Student):
        key = self.hash_key(student.id)
        if not self.table[key]:
            self.table[key] = Node(student)
        else:
            curr_node = self.table[key]
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = Node(student)
    
    #get info by ID
    def get_student_info(self, id: str) -> Student:
        key = self.hash_key(id)
        curr_node = self.table[key]
        while curr_node:
            if curr_node.student.id == str(id):
                return curr_node.student
            curr_node = curr_node.next
        return None


#load function
def load_student_info(filename: str, hashtable: HashTable):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            id, name, dob = line.strip().split(',')
            student = Student(id, name, dob)
            hashtable.insert(student)


#display student info by ID
def display_student_info(hashtable: HashTable):
    id = input("Enter the student code: ")
    student = hashtable.get_student_info(id)
    if student:
        print("ID:", student.id)
        print("Name:", student.name)
        print("Date of Birth:", student.dob)
    else:
        print("Student not found.")


def main():
    filename = "Sinhvien.txt"
    
    hashtable = HashTable()
    load_student_info(filename, hashtable)
    
    display_student_info(hashtable)


if __name__ == "__main__":
    main()