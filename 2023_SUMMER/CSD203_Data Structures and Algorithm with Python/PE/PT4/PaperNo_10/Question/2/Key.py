import math
from Student import *
from Node import *
from MyQueue import *

class BSTree:
    def __init__(self):
        self.root = None
    
    def clear(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def visit(self, p):
        if p is None:
            return
        print(f"{p.data}", end=" ")
    
    def preOrder(self, p):
        if p is None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    
    def preVisit(self):
        self.preOrder(self.root)
        print("")
    
    def postOrder(self, p):
        if p is None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    
    def postVisit(self):
        self.postOrder(self.root)
        print("")
    
    def inOrder(self, p):
        if p is None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)
    
    def inVisit(self):
        self.inOrder(self.root)
        print("")
    
    def breadth_first(self):
        if self.isEmpty():
            return
        my_queue = MyQueue()
        my_queue.EnQueue(self.root)
        while not my_queue.isEmpty():
            p = my_queue.DeQueue()
            self.visit(p)
            if p.left is not None:
                my_queue.EnQueue(p.left)
            if p.right is not None:
                my_queue.EnQueue(p.right)
        print("")
    
    def insert(self, name, age):
        # === YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ===
        if name.lower().startswith("x") or age < 15:
            return
        
        new_student = Student(name, age)
        new_node = Node(new_student)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if age < current.student.age:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right
    
    def f2(self):
        # === YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ===
        self.inOrder(self.root)
        print("")
    
    def f3(self):
        # === YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3 ===
        if self.root is not None and math.isqrt(self.root.student.age) ** 2 == self.root.student.age:
            self.root = self.deleteNode(self.root)
        self.preOrder(self.root)
        print("")
    
    def f4(self):
        # === YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4 ===
        self.inOrder(self.root)
        print("")
    
    def deleteNode(self, node):
        if node is None:
            return node
        
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        
        min_right = self.findMin(node.right)
        node.student = min_right.student
        node.right = self.deleteNode(node.right, min_right.student.age)
        
        return node
    
    def findMin(self, node):
        current = node
        while current.left:
            current = current.left
        return current