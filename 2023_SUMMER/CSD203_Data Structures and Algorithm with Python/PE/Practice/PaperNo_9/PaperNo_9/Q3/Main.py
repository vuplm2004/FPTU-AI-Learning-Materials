from Graph import *
import re
class Main:
    def __init__(self,fileName):
        self.fileName = fileName
        self.data = []
        self.lineNumber =0
    #end def    
    def readFile(self, lineStart):
        f1 = open(self.fileName,'r');
        count =0
        while True:        
            count+=1
            line = f1.readline()
            if not line:
                break
            if count== lineStart:
                lineNumber = int(line)                
                for i in range(lineNumber): 
                    line = f1.readline()                    
                    listValue = re.sub("\s+"," ",line.strip()).split(" ")                
                    row =[]
                    for j in range(len(listValue)):                        
                        row.append(int(listValue[j]))
                    self.data.append(row)
        f1.close()
        for i in range (len(self.data)):
            for j in range(i,len(self.data)):
                self.data[j][i] = self.data[i][j]
    def display(self):
        for line in self.data:
            [print(x, end=" ") for x in line]   
            print()     
                # listName = line.strip().split(", ")
    def clear(self):
        self.data =[]
        self.lineNumber = 0
    
#####################            
m = Main("input.txt")
print("1. Test f1 (1 mark)")
print("2. Test f2 (1 mark)")
choice = int(input("Your selection (1->2)"))
print("OUTPUT")
if choice ==1:    
    m.readFile(2)
    # m.display()
    g = Graph(m.data)
    g.f1("A")
elif choice ==2:
    m.clear()
    m.readFile(12)
    # m.display()
    g = Graph(m.data)
    g.f2("A","E")    
else:
    print("Wrong select")
print("FINISH")    