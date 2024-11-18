'''
STACK: First in last out (FILO)/ Last in first out (LIFO)
'''
import sys

class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        item = self.elements[-1]
        del self.elements[-1]
        return item

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

    def get_stack(self):
        return self.elements

if __name__ == "__main__":
    print("1 Push \
          \n2 Pop \
          \n3 Size \
          \n4 Empty \
          \n5 Get Stack")
    stack = Stack()
    
    while(1):
        try:
            action = int(input("Enter Action: "))
        except ValueError:
            print("Invalid Input. Try Again!")
            continue

        if action == 1:
            item = input("Push Item: ")
            if item:
                stack.push(item)
        elif action == 2:
            if stack.is_empty():
                print("Error: Stack is Empty.")
            else:
                print("Pop---> ", stack.pop())
        elif action == 3:
            print("Size---> ", stack.size())
        elif action == 4:
            print("Empty---> ", stack.is_empty())
        elif action == 5:
            print("Stack---> ", stack.get_stack())
        else:
            print("Exiting!")
            sys.exit()


            
