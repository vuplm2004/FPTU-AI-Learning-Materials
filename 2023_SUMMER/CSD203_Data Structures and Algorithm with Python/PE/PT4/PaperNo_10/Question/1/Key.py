import math
from Student import *
from Node import *

class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head == None
    
    def traverse(self):
        pt = self.head
        while pt:
            print(pt.data, end=" ")
            pt = pt.next
        print("")
    
    def clear(self):
        self.head = None
    
    # Q1-1
    def addLast(self, name="", age=-1):
        # === YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ===
        if name.startswith("Z") or age > 120:
            return

        new_student = Student(name, age)
        if self.isEmpty():
            self.head = new_student
            self.tail = new_student
        else:
            self.tail.next = new_student
            self.tail = new_student
    
    # Q1-2
    def addNode(self, name="", age=-1):
        # === YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ===
        if age % 2 == 0:
            current = self.head
            while current and current.age % 2 == 0:
                current = current.next
            new_student = Student(name, age)
            if not current:
                self.addLast(name, age)
            else:
                new_student.next = current.next
                current.next = new_student
    
    # Q1-3
    def delete(self):
        # === YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3 ===
        current = self.head
        if current and math.isqrt(current.age) ** 2 == current.age:
            self.head = current.next
        while current and current.next:
            if math.isqrt(current.next.age) ** 2 == current.next.age:
                current.next = current.next.next
            current = current.next
    
    # Q1-4
    def sort(self):
        # === YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4 ===
        odd_students = []
        current = self.head
        while current:
            if current.age % 2 == 1:
                odd_students.append(current)
            current = current.next
        
        odd_students.sort(key=lambda x: x.age, reverse=True)
        
        new_list = MyList()
        for student in odd_students:
            new_list.addLast(student.name, student.age)
        
        self.head = new_list.head
        self.tail = new_list.tail