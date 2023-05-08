#Binary Tree Implementation

class Node:
    
    def __init__(self, data) -> None:       
        self.data = data
        self.left = None
        self.right = None
    
    #function to insert item into binary tree.
    #building the function so if the item is less than the node it goes to the left, 
    # greater than goes to the right
    def insert(self, data):
        if self.data:
            if data < self.data:
                #traverse left
                if not self.left:
                      self.left = Node(data)
                else:
                      self.left.insert(data)
    
            elif data > self.data:
                #traverse right
                if not self.right:
                     self.right = Node(data)
                else:
                     self.right.insert(data)
    
    #Printing out the tree.
    #using inorder traversal to start
    #inorder traversal goes left then root then right
    #inorder of least to greatest
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
             self.right.printTree()
    

root = Node(12)
root.insert(6)
root.insert(15)
root.printTree()

                

