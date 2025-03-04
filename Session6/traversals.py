class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, treenode):
        self.children.append(treenode)

node_1 = BinaryTree("Drinks")
node_2 = BinaryTree("Hot")
node_3 = BinaryTree("Cold")
node_4 = BinaryTree("Tea")
node_5 = BinaryTree("Coffee")
node_6 = BinaryTree("Alcoholic")
node_7 = BinaryTree("Non-Alcoholic")
node_8 = BinaryTree("Beer")
node_9 = BinaryTree("Wine")
node_10 = BinaryTree("Soda")
node_11 = BinaryTree("Water")

node_1.add_child(node_2)
node_1.add_child(node_3)
node_2.add_child(node_4)
node_2.add_child(node_5)
node_3.add_child(node_6)
node_3.add_child(node_7)
node_6.add_child(node_8)
node_6.add_child(node_9)
node_7.add_child(node_10)
node_7.add_child(node_11)

print(node_1)

class Traversal:
    def preorder(self, root):
        if root is not None:
            print(root.data)
            for child in root.children:
                self.preorder(child)

    def postorder(self, root):
        if root is not None:
            for child in root.children:
                print("child",child.data)
                self.postorder(child)
            print(root.data)

    def inorder(self, root):
        if root is not None:
            if len(root.children) > 0:
                self.inorder(root.children[0])
            print(root.data)
            if len(root.children) > 1:
                self.inorder(root.children[1])

# Create an instance of Traversal and perform traversals
traversal = Traversal()

print("Preorder Traversal:")
traversal.preorder(node_1)

print("\nPostorder Traversal:")
traversal.postorder(node_1)

print("\nInorder Traversal:")
traversal.inorder(node_1)