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

    # Q1-1
    def addLast(self, name="", age=-1):
        if name.endswith("X") or age > 90:
            return

        new_customer = Customer(name, age)

        if self.isEmpty():
            self.head = self.tail = Node(new_customer)
        else:
            new_node = Node(new_customer)
            new_node.next = self.head
            self.head = new_node

    # Q1-2
    def addNode(self, name="", age=-1):
        if self.head is None:
            self.head = self.tail = Node(Customer(name, age))
        else:
            current = self.head
            while current.next and current.next.data.age % 2 != 0:
                current = current.next

            new_node = Node(Customer(name, age))
            new_node.next = current.next
            current.next = new_node

    # Q1-3
    def delete(self):
        if self.isEmpty():
            return

        if self.head.data.age in get_perfect_numbers():
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data.age in get_perfect_numbers():
                current.next = current.next.next
                return
            current = current.next

    # Q1-4
    def sort(self):
        def is_fibonacci(n):
            return math.isqrt(5 * n ** 2 + 4) % 1 == 0 or math.isqrt(5 * n ** 2 - 4) % 1 == 0

        if self.isEmpty() or self.head == self.tail:
            return

        prev = None
        current = self.head

        while current:
            if not is_fibonacci(current.data.age):
                break
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current.next = self.head
        self.head = current

        while current and current.next:
            if is_fibonacci(current.next.data.age):
                current = current.next
            else:
                prev = current
                current = current.next
                while current and not is_fibonacci(current.data.age):
                    prev = current
                    current = current.next

                if current is None:
                    return

                prev.next = current.next
                current.next = prev.next.next
                prev.next.next = current

def get_perfect_numbers():
    perfect_numbers = []
    for num in range(1, 100):
        sum_of_divisors = sum(
            divisor for divisor in range(1, num) if num % divisor == 0
        )
        if sum_of_divisors == num:
            perfect_numbers.append(num)
    return perfect_numbers
