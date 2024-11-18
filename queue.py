'''
QUEUE: first in first out (FIFO)
'''
import sys

class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self,item):
        self.elements.append(item)

    def dequeue(self):
        item = self.elements.pop(0)
        return item

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

    def get_queue(self):
        return self.elements

if __name__ == "__main__":
    queue = Queue()
    print("1 Enqueue \
          \n2 Dequeue \
          \n3 Size \
          \n4 Display \
          \n5 Empty")
    
    while(1):
        try:
            action = int(input("Choose Action: "))
        except:
            print("Invalid Input. Try Again!")
            continue
        
        if action == 1:
            item = input("Enqueue item: ")
            if item:
                queue.enqueue(item)
        elif action == 2:
            if queue.is_empty():
                print("Error: Queue is Empty.")
            else:
                print("Dequeue----> ", queue.dequeue())
        elif action == 3:
            print("Size----> ", queue.size())
        elif action == 4:
            print("Queue----> ", queue.get_queue())
        elif action == 5:
            print("Empty----> ", queue.is_empty())
        else:
            print("Exiting!")
            sys.exit()

