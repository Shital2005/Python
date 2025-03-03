# without size limit
# push
# pop
# peek
# isEmpty
# isFull
# Delete
# Display

import sys
class Stack:
    def __init__(self):
        self.stackList = []  #list representing a stack

    def push(self,value):
        self.stackList.append(value)

    def displayStack(self):
        print(self.stackList)   

    def isEmpty(self):
        if self.stackList == []:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            print(self.stackList.pop())

    def peek(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            print(self.stackList[-1])

    def deleteStack(self):
        self.stackList = []

    
obj = Stack()
print('Stack created')
while True:
    print('1.Push operation:')
    print('2.Pop operation:')
    print('3.Peek operation:')
    print('4.isEmpty operation:')
    print('5.Delete operation:')
    print('6.Display operation:')
    print('7.Exit Operation:')
    ch = int(input('Enter your choice:'))

    if ch == 1:
        value = int(input('Enter the value to be pushed:'))
        obj.push(value)
        print('Value pushed successfully')

    elif ch == 2:
        obj.pop()

        
    elif ch == 3:
        obj.peek()

    elif ch == 4:
       print(obj.isEmpty())

    elif ch == 5:
        obj.deleteStack()

    elif ch == 6:
        obj.displayStack()

    elif ch == 7:
        sys.exit()

    else:
        print('Invalid choice')
        sys.exit()



      



