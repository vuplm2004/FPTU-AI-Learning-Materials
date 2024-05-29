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
        


        pass 
    def f2(self):        
       # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2========




        pass    
    def f3(self):
    # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3========


        pass
    def f4(self):
    # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4========



        pass               
# end class
