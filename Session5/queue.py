# Queue implementation with size 
# enqueue
# dequeue
# Peek(return first element)
# isEmpty
# isFull
# Delete queue
# Display queue
# Exit

class Queue:
    def __init__(self, size):
        self.queueList = []  # list representing a queue
        self.maxsize = size

    def isFull(self):
        if len(self.queueList) == self.maxsize:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            print('Queue is full')
        else:
            self.queueList.append(value)
            print('Value enqueued successfully')

    def displayQueue(self):
        print(self.queueList)

    def isEmpty(self):
        if self.queueList == []:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            print('Queue is empty')
        else:
            print(self.queueList.pop(0))

    def peek(self):
        if self.isEmpty():
            print('Queue is empty')
        else:
            print(self.queueList[0])

    def deleteQueue(self):
        self.queueList = []

size = int(input('Enter the size of the queue: '))
obj = Queue(size)
print('Queue created')
while True:
    print('1.Enqueue operation:')
    print('2.Dequeue operation:')
    print('3.Peek operation:')
    print('4.isEmpty operation:')
    print('5.Delete operation:')
    print('6.Display operation:')
    print('7.Exit Operation:')
    print('8.Is Full?:')

    ch = int(input('Enter your choice:'))

    if ch == 1:
        value = int(input('Enter the value to be enqueued:'))
        obj.enqueue(value)

    elif ch == 2:
        obj.dequeue()

    elif ch == 3:
        obj.peek()

    elif ch == 4:
        print(obj.isEmpty())

    elif ch == 5:
        obj.deleteQueue()

    elif ch == 6:
        obj.displayQueue()

    elif ch == 7:
        break

    elif ch == 8:
        print(obj.isFull())

    else:
        print('Invalid choice, please try again.')







