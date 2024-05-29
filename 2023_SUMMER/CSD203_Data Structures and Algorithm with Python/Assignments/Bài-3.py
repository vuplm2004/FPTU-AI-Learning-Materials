class Stack:
    def __init__(self):
        self.stack = []
        
    def size(self):
        return len(self.stack)
    
    def is_mpt(self):
        if len(self.stack)==0:
            return True
        return False
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        #Check wthr the stack is mpt or not before pop
        if not self.is_mpt():
            self.stack.pop()
        else:
            print("Stack is empty")
        
    def display(self):
        #Print in reverse order
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i], end ='')
            
    def dec_2_bin(self, dec):
        while dec !=0:
            self.push(dec%2)
            dec = dec//2
            
new_stack = Stack()
num = int(input('ENTER THE NUMBER: '))
new_stack.dec_2_bin(num)
new_stack.display()
