# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.item)


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)


    def inorder(self, node):
        if node is None:
            return []
        result = [node.item]
        left_item = self.inorder(node.left)
        right_item = self.inorder(node.right)
        return left_item + result + right_item


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    print(tree.inorder(tree.root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
