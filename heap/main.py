# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class heap:
    def __init__(self):
        self.data_list = []

    def get_parent_index(self, index):
        if index == 0 or index > len(self.data_list):
            return -1
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        # 循环，直到该元素成为堆顶，或小于父节点（对于大顶堆)
        while parent is not None and self.data_list[parent] < self.data_list[index]:
            # 交换操作
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def removeMax(self):
        # 删除堆顶元素，然后将最后一个元素放在堆顶，再从上往下依次堆化
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]

        # 堆化
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        # 从上往下堆化，从index 开始堆化操作 (大顶堆)
        total_index = len(self.data_list) - 1
        while True:
            maxvalue_index = index
            if 2*index + 1 <= total_index and self.data_list[2*index + 1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index + 1
            if 2*index + 2 <= total_index and self.data_list[2*index + 2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index + 2
            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myheap = heap()
    for i in range(10):
        myheap.insert(i+1)
    print('建堆:', myheap.data_list)
    print("删除堆顶元素：", [myheap.removeMax() for _ in range(10)])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
