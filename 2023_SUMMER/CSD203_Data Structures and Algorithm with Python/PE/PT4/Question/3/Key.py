import math
from Stack import *

class Graph:
    def __init__(self, data):
        self.a = data

    def display(self):
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                print(self.a[i][j], end=" ")
            print("")
        print("")

    def f1(self):
        self.depthFirst2(1)
        print("FINISH")

    def depthFirst2(self, start):
        visited = [False] * len(self.a)
        degrees = [0] * len(self.a)
        self.depth2(start, visited, degrees)
        print("")

    def depth2(self, start, visited, degrees):
        visited[start] = True
        print(f"{chr(start + 65)}", end=" ")

        if degrees[start] % 2 == 0:
            print(f"({degrees[start]})", end=" ")

        for i in range(len(self.a)):
            if self.a[start][i] != 0 and not visited[i]:
                visited[i] = True
                degrees[i] = self.deg(i)
                self.depth2(i, visited, degrees)

    def deg(self, x):
        count = 0
        for i in range(len(self.a)):
            count += self.a[x][i]
        return count

    def f2(self):
        cycle = self.findEulerCycle(1)
        degrees = [0] * len(self.a)
        for v in cycle:
            degrees[v] = self.deg(v)
        for i, v in enumerate(cycle):
            if degrees[v] > 2:
                print(f"{chr(v + 65)}({degrees[v]})", end=" ")
            else:
                print(f"{chr(v + 65)}", end=" ")
        print("FINISH")

    def findEulerCycle(self, startV):
        S = Stack()
        E = []
        S.push(startV)

        while not S.isEmpty():
            r = S.top()

            if self.isIsolated(r):
                S.pop()
                E.append(r)
            else:
                for i in range(len(self.a)):
                    if self.a[r][i] != 0:
                        nextV = i
                        self.a[r][i] = 0
                        break
                S.push(nextV)

        return E

    def isIsolated(self, v):
        for i in range(len(self.a)):
            if self.a[v][i] != 0:
                return False
        return True
