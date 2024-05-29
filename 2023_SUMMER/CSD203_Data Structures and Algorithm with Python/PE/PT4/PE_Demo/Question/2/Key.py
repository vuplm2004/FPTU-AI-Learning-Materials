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

    def visit(self, p):
        if p == None:
            return
        print(f"{p.data}", end=" ")

    def preOrder(self, p):
        if p == None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)

    def preVisit(self):
        self.preOrder(self.root)
        print("")

    def postOrder(self, p):
        if p == None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)

    def postVisit(self):
        self.postOrder(self.root)
        print("")

    def inOrder(self, p):
        if p == None:
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
            if p.left != None:
                my.EnQueue(p.left)
            if p.right != None:
                my.EnQueue(p.right)
        print("")

    def insert(self, name, price):
        if name.startswith("G") or price < 0:
            return

        new_product = Product(name, price)
        new_node = Node(new_product)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if price < current.data.price:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def f2(self):
        self.inOrderOddHeight(self.root, 1)
        print("FINISH")

    def f3(self):
        self.postOrderDeleteFibonacci(self.root)
        self.inOrder(self.root)
        print("FINISH")

    def f4(self):
        self.inOrderRotatePerfectNumber(self.root)
        self.inOrder(self.root)
        print("FINISH")

    def inOrderOddHeight(self, node, height):
        if node is None:
            return

        self.inOrderOddHeight(node.left, height + 1)
        if node.data.price % 2 != 0:
            print(f"({node.data.name}, {node.data.price})({height}) ", end="")
        self.inOrderOddHeight(node.right, height + 1)

    def postOrderDeleteFibonacci(self, node):
        if node is None or (node.left is None and node.right is None):
            return node

        node.left = self.postOrderDeleteFibonacci(node.left)
        node.right = self.postOrderDeleteFibonacci(node.right)

        if (
            node.left is not None
            and node.left.left is not None
            and is_fibonacci(node.left.data.price)
        ):
            node.left = node.left.left

        return node

    def inOrderRotatePerfectNumber(self, node):
        if node is None or (node.left is None and node.right is None):
            return node

        node.left = self.inOrderRotatePerfectNumber(node.left)
        node.right = self.inOrderRotatePerfectNumber(node.right)

        if (
            node.left is not None
            and node.right is not None
            and is_perfect_number(node.data.price)
        ):
            temp = node.right
            node.right = temp.left
            temp.left = node
            return temp

        return node


def is_fibonacci(n):
    return math.isqrt(5 * n ** 2 + 4) % 1 == 0 or math.isqrt(5 * n ** 2 - 4) % 1 == 0


def is_perfect_number(n):
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n
