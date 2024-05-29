import math
from Customer import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(a):
        return a.head ==None
    def traverse(a):
        pt = a.head
        while pt:
            print(pt.data, end = " ")
            pt = pt.next
        print("")        
    def clear(self):
        self.head = None
#Q1-1
    def addLast(a, name="", age=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        if name[-1] == 'X' or age > 90:
            return
        n = Node(Customer(name,age))
        if (a.isEmpty()):
            a.head = a.tail = n
        else:
            a.tail.next = n
            a.tail = n
        
        pass
    # end def
#Q1-2    
    def addNode(self, name="", age=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        new_node = Node(data = Customer(name, age))
        if not self.head or self.head.data.Age % 2 == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            count = 0
            while current.next:
                if current.next.data.Age % 2 != 0:
                    count += 1
                    prev = current
                    if count == 1:
                        new_node.next = prev.next
                        prev.next = new_node
                        break
                current = current.next

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