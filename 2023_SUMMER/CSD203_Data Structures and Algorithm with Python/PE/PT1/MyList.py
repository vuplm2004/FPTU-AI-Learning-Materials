import math
from Student import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def traverse(self):
        pt = self.head
        while pt:
            print(pt.data, end = " ")
            pt = pt.next
        print("")        
    def clear(self):
        self.head = None
#Q1-1
    def addFirst(self, name="", age=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        if not name.endswith('Z') and age <= 120:
            s = Student(name, age)
            p = Node(s)
            if self.isEmpty():
                self.head = self.tail = p
            else:
                p.next = self.head
                self.head = p
        

        pass
    # end def
#Q1-2    
    def addNode(self, name="", age=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        




        pass
    # end def
#Q1-3
    def delete(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3 ========




        pass 
    #end def
# Q1-4
    def sort(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4 ========



        
         pass
    #end def    