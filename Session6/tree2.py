# import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def _str_(self,level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.childern:
            ret += child._str_(level + 1)
        return ret


newBT = TreeNode("Drinks")
leftChild =TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild  = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data, end = " ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end = " ")
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data,end= " ")

inOrderTraversal(newBT) 
preOrderTraversal(newBT)
postOrderTraversal(newBT)




