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

    def __init__(self,size):
        self.stackList = []  #list representing a stack
        self.maxsize = size

    def isFull(self):
        if len(self.stackList) == self.maxsize:
            return True
        else:
            return False

    def push(self,value):
        if self.isFull():
            print('Stack is full')
        else:
           self.stackList.append(value)
           print('Value pushed successfully')

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

size = int (input('Enter the size of the stack:'))
obj = Stack(size)
print('Stack created')
while True:
    print('1.Push operation:')
    print('2.Pop operation:')
    print('3.Peek operation:')
    print('4.isEmpty operation:')
    print('5.Delete operation:')
    print('6.Display operation:')
    print('7.Exit Operation:')
    print('8.Is Full?:')

    ch = int(input('Enter your choice:'))

    if ch == 1:
        value = int(input('Enter the value to be pushed:'))
        obj.push(value)

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

    elif ch == 8:
        print(obj.isFull())
    
    else:
        print('Invalid choice')
        sys.exit()



      



