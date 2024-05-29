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
        if name[-1] != 'Z' and age <= 120:
            new_node = Node(Student(name, age))
            new_node.next = self.head
            self.head = new_node
        curr = self.head
        while curr.next:
            curr = curr.next
        self.tail = curr
        pass
    # end def
#Q1-2    
    def addNode(self, name="", age=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        new_node = Node(Student(name,age))
        curr = self.head
        lastNode = None
        while curr:
            if curr.data.Age % 2 == 0:
                lastNode = curr
            curr= curr.next
        if lastNode is None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = lastNode.next
            lastNode.next = new_node
        



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