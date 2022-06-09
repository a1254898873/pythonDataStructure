# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def is_empty(self):
        if self.head:
            return False
        else:
            return True

    def insert(self, position, new_element):
        if position < 0:
            raise IndexError("插入位置越界")
        if position == 0:
            temp = self.head
            self.head = new_element
            self.head = temp
            return

        index = 0
        current = self.head
        while index < position:
            index = index + 1
            pre = current
            current = current.next
        pre.next = new_element
        new_element.next = current

    def remove(self, position):
        if position < 0:
            raise IndexError("插入位置越界")

        index = 0
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp.next = None
            return

        while temp != None:
            pre = temp
            temp = temp.next
            index += 1
            if index == position:
                pre.next = temp.next
                temp.next = None
                return

    def get_length(self):
        temp = self.head
        length = 0
        while temp != None:
            temp = temp.next
            length += 1

        return length

    def print(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    node1 = Node(1)
    linklist = LinkList(node1)
    node2 = Node(2)
    node3 = Node(3)
    linklist.insert(1,node2)
    linklist.insert(1,node3)
    linklist.print()



