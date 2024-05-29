import math
from Product import *
from Node import *
from MyQueue import *

class BSTree:
    def __init__(self):
        self.root = None
    
    def clear(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def visit(self,p):
        if p==None:
            return
        print(f"({p.data.Name}, {p.data.Price})",end =" ")
    
    def preOrder(self,p):
        if p==None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    
    def preVisit(self):
        self.preOrder(self.root)
        print("")
    
    def postOrder(self,p):
        if p==None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    
    def postVisit(self):
        self.postOrder(self.root)
        print("")
    
    def inOrder(self,p):
        if p==None:
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
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            self.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("")        
    
    def insert(self,name, price):        
        if name[0] == "G" or  price < 0:
            return
        newNode = Node(data = Product(name, price))
        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            while current:
                if price < current.data.Price:
                    if current.left:
                        current = current.left
                    else:
                        current.left = newNode
                        break
                elif price > current.data.Price:
                    if current.right:
                        current = current.right
                    else:
                        current.right = newNode
                        break
                else:
                     break
    
    def f1(self):
        self.insert("F",25)
        self.insert("B",26)
        self.insert("A",35)
        self.insert("D",33)
        self.insert("C",33)
        self.insert("E",24)
        self.insert("Y",105)
        self.insert("X",56)
        self.inVisit()
        self.postVisit()
        print("FINISH")
    
    def f2(self):
        self.inOrder2(self.root)
        print("")
    
    def inOrder2(self,p):
        if p==None:
            return
        h = self.height(p)
        self.inOrder2(p.left)
        if p.data.Price % 2 ==1:
            print(f"({p.data.Name}, {p.data.Price})({h})",end =" ")
        self.inOrder2(p.right)
        
    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1
    
    def f3(self):
        p = self.search_f3()
        self.delByCopyLeft(p)
    
    def search_f3(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and self.is_fibonacci_number(p.data.Price):
                count += 1
            if count == 2:
                return p
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        return None
    
    def is_fibonacci_number(self,num):
        if num < 0:
            return False
        a, b = 0, 1
        while b < num:
            a, b = b, a + b
        return b == num
    
    def delByCopyLeft(self,p):
        if not p:
            return
        rightmost = p.left
        parent = None
        while rightmost.right:
            parent = rightmost
            rightmost = rightmost.right
        p.data = rightmost.data
        if parent:
            parent.right = rightmost.left
        else:
            p.left = rightmost.left
    
    def f4(self):
        my = MyQueue()
        if self.root is None:
            return
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
           I apologize for the incomplete response. Here is the completed `f4` method:
    def f4(self):
        my = MyQueue()
        if self.root is None:
            return
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.right:
                if p.left.data.Price > p.right.data.Price:
                    p.left.data, p.right.data = p.right.data, p.left.data
            if p.left:
                my.EnQueue(p.left)
            if p.right:
                my.EnQueue(p.right)
        self.inVisit()