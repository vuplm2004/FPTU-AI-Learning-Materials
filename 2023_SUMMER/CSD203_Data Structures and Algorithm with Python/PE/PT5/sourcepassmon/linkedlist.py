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
            new_node = Node(Pro(name, age))
            new_node.next = self.head
            self.head = new_node
        curr = self.head
        while curr.next:
            curr = curr.next
        self.tail = curr
        pass
    # end def
    def addLast(self, name, age):
        if name[-1] != 'Z' and age <= 120:
        n = Node(Student(name,age))
        if (self.isEmpty()):
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n
##########################################################
    def addAfterFirst(self, name, age):
        new_node = Node(data=Student(name, age))
        if self.head == None:
            self.head = new_node
            return
        cur = self.head
        while cur:
            if cur.data.Age % 2 == 0:
                new_node.next = cur.next
                cur.next = new_node
                break
            cur = cur.next
    def addAfterSecond(self, name, age):
        newnode = Node(data = Student(name, age))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            curr = self.head
            prev = None
            count = 0
            while curr:
                if curr.data.Age % 2 == 0:
                    count += 1
                    if count == 2: #count bằng bao nhiêu thì thứ tự bấy nhiêu
                        newnode.next = curr.next
                        curr.next = newnode
                        break
                prev = curr
                curr = curr.next
            if curr is None and prev is not None:
                prev.next = new
    def addAfterLast(self, name, age):
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
    def addBeforeFirst(self, name, age):
        new_node = Node(data = Student(name, age))
        if not self.head or self.head.data.Age % 2 == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev = None
            while curr:
                if curr.data.Age % 2 == 0:
                    if prev is None:
                        new_node.next = curr
                    else:
                        prev.next = new_node
                        new_node.next = curr
                    break
                prev = curr
                curr = curr.next
    def addBefore2nd(self, name, age):
        new_node = Node(data = Student(name, age))
        if not self.head or self.head.data.Age % 2 == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            count = 0
            while current.next:
                if current.next.data.Age % 2 == 0:
                    count += 1
                    prev = current
                    if count == 2:
                        new_node.next = prev.next
                        prev.next = new_node
                        break
                current = current.next
    def addBeforeLast(self, name, age):
        new_node = Node(Student(name, age))
        curr = self.head
        prev = None
        lastNode = None
        while curr.next:
            if curr.next.data.Age % 2 == 0:
                prev = curr
                lastNode = curr.next
            curr = curr.next
        if lastNode is None:  # No node with even age found
            new_node.next = self.head
            self.head = new_node
        else:
            if lastNode == self.head:  # Last node is the head node
                new_node.next = self.head
                self.head = new_node
            else:
                prev.next = new_node
                new_node.next = lastNode
