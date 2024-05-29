import math
from Product import *
from Node import *
from MyQueue import *
class BSTree:
    def __init__(self):
        self.root = None
    # end def
    def clear(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    #end def
    def visit(self,p):
        if p==None:
            return
        print(f"{p.data}",end =" ")
    #end def
    def preOrder(self,p):
        if p==None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    #end def
    def preVisit(self):
        self.preOrder(self.root)
        print("")
    #end def
    def postOrder(self,p):
        if p==None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    #end def
    def postVisit(self):
        self.postOrder(self.root)
        print("")
    #end def
    def inOrder(self,p):
        if p==None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)        
    #end def
    def inVisit(self):
        self.inOrder(self.root)
        print("")
    #end def
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
    #end def
    def insert(self,name, price):        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        newNode = Node(data = Product(name, price))
        if name[0] == "G" or  price < 0:
        # Sửa điều kiện theo đề bài yêu cầu
            return
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


        pass 
    def f2(self):        
       # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2========
        self.inOrder2(self.root)
        print("")
    def inOrder2(self,p):
        if p==None:
            return
        h = self.height(p)
        self.inOrder2(p.left)
        if p.data.Price % 2 ==1:
            print(f"{p.data}({h})",end =" ")
        self.inOrder2(p.right)
        
    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1
    def f3(self):
    # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3========
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
            #Sửa điều kiện theo yêu cầu đề bài
                count += 1
            if count == 2:
            # Đề yêu cầu là node thứ mấy thì count bằng bấy nhiêu (ví dụ đề yêu cầu 'first node' thì count = 1
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
            pass
##############Delete by Copy                
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

        pass
    def f4(self):
    # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4========
        
        
        pass
    

# end class
