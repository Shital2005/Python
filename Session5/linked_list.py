class Node:
    #to create the node
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    #to link the linked list
    def __init__(self):
        self.head = None 

linkObj = LinkedList()
linkObj.head = Node(10)
second = Node(20)
third = Node(30)


#connect nodes 

linkObj.head.next = second
second.next = third

while linkObj.head is not None:
    print(linkObj.head.data,"->",end = " ")
    linkObj.head = linkObj.head.next


