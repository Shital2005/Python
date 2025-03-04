# import sys

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def addnode(self, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = node

#     def addNodeBeginning(self, value):
#         node = Node(value)
#         if self.head is None:
#             self.head = node
#             self.tail = node
#         else:
#             node.next = self.head
#             self.head = node

#     def addInBetween(self,prev_value,value):
#         # current = self.head
#         # while current is not None:
#         #     if current.data == prev_value:
#         #         node = Node(value)
#         #         node.next = current.next
#         #         current.next = node
#         #         if node.next is None:
#         #             self.tail = node
#         #             print(f"node added successfully after {prev_value}")
#         #             return 
#         #         current = current.next
#         #         print(f"node with value {prev_value } not found ")

        
#     # def addNodeEnd(self,value):
#     #     node = Node(value)
#     #     if self.head is None:
#     #         self.head = node
#     #         self.tail = node
#     #     else:
#     #         self.tail.next = node
#     #         self.tail = node
#     #     print("Node added successfully at the end")


#     # def displayNode(self):
#     #     current = self.head
#     #     while current is not None:
#     #         print(current.data, "->", end=' ')
#     #         current = current.next
#     #     print("None")
 
# if __name__ == '__main__':
#     object = LinkedList()

#     while True:
#         print("1. Add Node in LinkedList:")
#         print("2. Add Node in Beginning:")
#         print("3. Add Node in Between:")
#         print("4. Add Node in End")
#         print("5. Display Node")
#         print("6. Exit")

#         ch = int(input("Enter your choice: "))
#         if ch == 1:
#             value = int(input("Enter value for node: "))
#             object.addnode(value)
#             print("Node added successfully in single LinkedList")

#         elif ch == 2:
#             value = int(input("Enter value for node: "))
#             object.addNodeBeginning(value)
#             print("Node added successfully at the beginning of the LinkedList")

#         elif ch == 3:
#             prev_value = int(input("Enter prev value for node: "))
#             value = int(input("Enter value for node: "))

#             object.addInBetween(prev_value,value)

#         elif ch == 4:
#             value = int(input("Enter value for node: "))
#             object.addnode(value)
#             print("Node added successfully at the end of the LinkedList")

#         elif ch == 5:
#             object.displayNode()

#         elif ch == 6:
#             break

#         else:
#             print("Invalid choice, please try again.")