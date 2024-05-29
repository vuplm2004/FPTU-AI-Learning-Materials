class Queue:
    def __init__(self):
        self.queue = []
        
    def size(self):
        return len(self.queue)
    
    def is_mpt(self):
        if len(self.queue)==0:
            return True
        return False
    
    def front(self):
        return self.queue[0]
    
    def back(self):
        return self.queue[len(self.queue)-1]
    
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        #Check wthr the stack is mpt or not before dequeue
        if not self.mpt():
            self.queue.pop(0)
        else:
            print("Queue is empty")
        
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            for item in self.queue:
                print(item)
        
    def name_ticket(self):
        while True:
            name = input('Enter your name: ').lower()
            if name == 'none':
                return
            ticket = int(input('Enter the number of tickets you wanna buy: '))
            self.enqueue([name, ticket])
            
    def service(self):
        num_ticket = int(input('Enter the total number of tickets: '))
        for i in range(len(self.queue)):
            old_value = self.queue[i][-1]
            if num_ticket - self.queue[i][-1] > 0:
                new_num_ticket = self.queue[i][-1]
            elif num_ticket - self.queue[i][-1] <= 0 and num_ticket > 0:
                new_num_ticket = num_ticket
            elif num_ticket <= 0:
                new_num_ticket = 0
            if old_value == self.queue[i][-1]:
                self.queue[i][-1] = new_num_ticket
            num_ticket -= new_num_ticket
        
        
new_queue = Queue()
new_queue.service()
new_queue.name_ticket()

new_queue.display()

