class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if not current_node.left:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if not current_node.right:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("Already exists")

    # Inorder (left-root-right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(str(node.data), end=' ')
            self.inorder(node.right)

    # Preorder (root-left-right)
    def preorder(self, node):
        if node:
            print(str(node.data), end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder (left-right-root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(str(node.data), end=' ')

    # Search for a value in the bin tree
    def search(self, data):
        if not self.root:
            return False
        else:
            return self._search(data, self.root)

    def _search(self, data, current_node):
        if data == current_node.data:
            return True
        elif data < current_node.data and current_node.left:
            return self._search(data, current_node.left)
        elif data > current_node.data and current_node.right:
            return self._search(data, current_node.right)
        return False

if __name__ == '__main__':
    bst = BinTree()

    print("Enter consecutive integers pls:")
    nums = list(map(int, input().split()))
    for num in nums:
        bst.insert(num)

    print("\nInorder:")
    bst.inorder(bst.root)

    print("\nPreorder:")
    bst.preorder(bst.root)

    print("\nPostorder:")
    bst.postorder(bst.root)

    # Search for a number in the binary search tree
    print("\nEnter a number to search:")
    x = int(input())
    if bst.search(x):
        print("Number exists")
    else:
        print("Number does not exist")
        