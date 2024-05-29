import math
from Student import *
from Node import *
from MyQueue import *
class BSTree:
    def __init__(self):
        self.root = None
    # end def
    def clear(self):
        self.root = None
    def isEmpty(a):
        return a.root == None
    #end def
    def visit(a,p):
        if p==None:
            return
        print(f"{p.data}",end =" ")
    #end def
    def preOrder(a,p):
        if p==None:
            return
        a.visit(p)
        a.preOrder(p.left)
        a.preOrder(p.right)
    #end def
    def preVisit(a):
        a.preOrder(a.root)
        print("")
    #end def
    def postOrder(a,p):
        if p==None:
            return
        a.postOrder(p.left)
        a.postOrder(p.right)
        a.visit(p)
    #end def
    def postVisit(a):
        a.postOrder(a.root)
        print("")
    #end def
    def inOrder(a,p):
        if p==None:
            return
        a.inOrder(p.left)
        a.visit(p)
        a.inOrder(p.right)        
    #end def
    def inVisit(a):
        a.inOrder(a.root)
        print("")
    #end def
    def breadth_first(a):
        if a.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(a.root)
        while not my.isEmpty():
            p = my.DeQueue()
            a.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("")        
    #end def
    def insert(a,name, age):        
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        newNode = Node(data = Student(name, age))
        if name[0] == "X" or  age < 15:
        # Sửa điều kiện theo đề bài yêu cầu
            return
        if a.root is None:
            a.root = newNode
        else:
            current = a.root
            while current:
                if age < current.data.Age:
                    if current.left:
                        current = current.left
                    else:
                        current.left = newNode
                    
                        break
                elif age > current.data.Age:
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
        self.postOrder2(self.root)
        print("")
    def postOrder2(self,p):
        if p==None:
            return
        self.postOrder2(p.left)
        self.postOrder2(p.right)
        if p.data.Age % 2 == 0:
            print(f"{p.data}",end =" ")


        pass    
    def f3(self):
    # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3========
        p = self.search_f3()
        self.delByMergingLeft(p)
    
    def is_square(self, number):
        if number < 0:
            return False
        sqrt = int(number ** 0.5)
        return sqrt * sqrt == number
    def search_f3(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        count = 0
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.right and self.is_square(p.data.Age):
            #Sửa điều kiện theo yêu cầu đề bài
                count += 1
            if count == 1:
            # Đề yêu cầu là node thứ mấy thì count bằng bấy nhiêu (ví dụ đề yêu cầu 'first node' thì count = 1
                return p
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
    def delByMergingLeft(self,p):
        if p is None:
            return
        parent = self._find_parent(self.root, p)
        if parent is None:
            self.root = self.mergeLeftChild(p)
        elif parent.left == p:
            parent.left = self.mergeLeftChild(p)
        else:
            parent.right = self.mergeLeftChild(p)
    def mergeLeftChild(self, node):
        if node is None or node.left is None:
            return node

        leftChild = node.left
        if leftChild.right is None:
            node.left = leftChild.left
        else:
            parent = node.left
            while leftChild.right:
                parent = leftChild
                leftChild = leftChild.right
            parent.right = leftChild.left

        leftChild.left = node.left
        leftChild.right = node.right
        return leftChild
    def _find_parent(self, root, node):
        if not root:
            return None
        if root.left == node or root.right == node:             
            return root
        if node.data.Age < root.data.Age:
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)

        pass
    def f4(self):
    # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4========



        pass               
# end class
