# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.rear = None

    def is_empty(self):
        return not self.head

    def enqueue(self, elem):
        p = Node(elem)
        if self.is_empty():
            self.head = p
            self.rear = p
        else:
            self.rear.next = p
            self.rear = p

    def dequeue(self):
        if self.is_empty():
            raise IndexError("队列为空")
        else:
            result = self.head.elem
            self.head = self.head.next
            return result

    def peel(self):
        if self.is_empty():
            raise IndexError("队列为空")
        else:
            return self.head.elem


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(1)
    queue.enqueue(3)
    while not queue.is_empty():
        print(queue.dequeue())
