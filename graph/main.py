# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def insert(self, a, b):

        if not (a in self.nodes):
            self.nodes.append(a)
            self.edges[a] = list()
        if not (b in self.nodes):
            self.nodes.append(b)
            self.edges[b] = list()

        self.edges[a].append(b)
        self.edges[b].append(a)

    def succ(self, a):
        # 返回与 a 连接的点
        return self.edges[a]

    def show_nodes(self):
        # 返回图的点集
        return self.nodes

    def show_edge(self):
        print(self.edges)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    graph = Graph()
    graph.insert('0', '1')
    graph.insert('0', '2')
    graph.insert('0', '3')
    graph.insert('1', '3')
    graph.insert('2', '3')
    graph.show_edge()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
