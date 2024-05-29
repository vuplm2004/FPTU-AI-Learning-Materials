import math
from Customer import *
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
    
    def addLast(self, name="", age=-1):
        if name[-1] == 'X' or age > 90:
            return
        
        n = Node(Customer(name, age))
        if self.isEmpty():
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n
    
    def addNode(self, name="", age=-1):
        new_node = Node(data=Customer(name, age))
        
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
    
    def delete(self):
        if self.isEmpty():
            return
        
        if self.head.data.Age == self.getPerfectNumber():
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return
        
        current = self.head
        prev = None
        while current:
            if current.data.Age == self.getPerfectNumber():
                prev.next = current.next
                if not prev.next:
                    self.tail = prev
                break
            prev = current
            current = current.next
    
    def sort(self):
        def isFibonacci(n):
            sq1 = math.isqrt(5 * n * n - 4)
            sq2 = math.isqrt(5 * n * n + 4)
            return sq1 * sq1 == 5 * n * n - 4 or sq2 * sq2 == 5 * n * n + 4
        
        if self.isEmpty():
            return
        
        dummy = Node()
        dummy.next = self.head
        current = self.head
        sorted_tail = dummy
        temp = None
        
        while current:
            if not isFibonacci(current.data.Age):
                sorted_tail.next = current
                sorted_tail = current
                if not temp:
                    self.head = current.next
                else:
                    temp.next = current.next
                current = current.next
                sorted_tail.next = None
            else:
                temp = current
                current = current.next
        
        sorted_tail.next = self.head
        self.head = dummy.next
    
    def getPerfectNumber(self):
        # Function to get the first perfect number greater than 0 (which is 6)
        return 6
