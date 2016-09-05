
import datetime
import itertools
import re

class min_heap:
    def __init__(self):
        self.data = ['']
        self.count = 0

        self.i = 0
        self.smlchild = 0

    def swim(self, index):
        while index // 2 > 0:
            if self.data[index] < self.data[int(index // 2)]:
                tmp = self.data[int(index // 2)]
                self.data[int(index // 2)] = self.data[index]
                self.data[index] = tmp
            index = int(index // 2)

    def sink(self, index):
        while (index * 2) <= self.count:
            self.smlchild = self.smaller_child(index)
            if self.data[index] >= self.data[self.smlchild]:
                temp = self.data[self.smlchild]
                self.data[self.smlchild] = self.data[index]
                self.data[index] = temp
            index = self.smlchild

    def Remove(self, value):
        if (self.data[self.count] == value):
            self.data.pop()
            self.count = self.count - 1
        else:
            for j in range(1, self.count):
                if self.data[j] == value:
                    self.data[j] = self.data[self.count]
                    self.count = self.count - 1
                    self.data.pop()
                    self.sink(j)
                    self.swim(j)
                    self.sink(1)
                    break



    def smaller_child(self, i):
        if ((i * 2) + 1) > self.count:
            return (i * 2)
        else:
            if self.data[(i * 2)] > self.data[((i * 2) + 1)]:
                return ((i * 2) + 1)
            else:
                return (i * 2)

    def put(self, node):
        self.data.append(node)
        self.count = self.count + 1
        self.swim(self.count)



    def RemoveMin(self):
        min_data = self.data[1]
        self.data[1] = self.data[self.count]
        self.count = self.count - 1
        self.data.pop()
        self.sink(1)


        return min_data

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def size(self):
        return self.count

    def GetMin(self):
        if self.count > 0:
            return self.data[1]
        else:
            return 0

    def IsContain(self, name):
        if name in self.data:
            return True
        else:
            return False

    def BuiltMIN_HEAP(self, txtfile):

        with open(txtfile, 'r') as fh:
            next(fh)
            for line in fh:
                self.count = self.count + 1
                self.data.append(line.strip())
                print("Added [", self.count, "]", self.data[self.count])
        #fh = open(txtfile, 'r')

        #for f in fh.readlines():

        self.i = int(self.count // 2)
        print(self.i)
        while (self.i > 0):
            self.sink(self.i)
            self.i = (self.i) - 1

    def print_MIN_HEAP(self):
        print("Printing Min PQ")
        for i in range(1, self.count + 1):
            print("[", i, "]", self.data[i])


# **************MIn Heap Implementation Complete************************
class max_heap:
    def __init__(self):
        self.data = ['']
        self.count = 0
        self.i = 0
        self.bigchild = 0

    def swim(self, index):
        while index // 2 > 0:
            if self.data[index] > self.data[int(index // 2)]:
                tmp = self.data[int(index // 2)]
                self.data[int(index // 2)] = self.data[index]
                self.data[index] = tmp
            index = int(index // 2)

    def sink(self, index):
        while (index * 2) <= self.count:
            self.bigchild = self.bigger_child(index)
            if self.data[index] <= self.data[self.bigchild]:
                temp = self.data[self.bigchild]
                self.data[self.bigchild] = self.data[index]
                self.data[index] = temp
            index = self.bigchild

    def bigger_child(self, i):
        if ((i * 2) + 1) > self.count:
            return (i * 2)
        else:
            if self.data[(i * 2)] < self.data[((i * 2) + 1)]:
                return ((i * 2) + 1)
            else:
                return (i * 2)

    def put(self, node):
        self.data.append(node)
        self.count = self.count + 1
        self.swim(self.count)


    def RemoveMax(self):
        max_data = self.data[1]
        self.data[1] = self.data[self.count]
        self.count = self.count - 1
        self.data.pop()
        self.sink(1)

        return max_data

    def Remove(self, value):
        if (self.data[self.count] == value):
            self.data.pop()
            self.count = self.count - 1
        else:
            for j in range(1, self.count):
                if (self.data[j] == value):
                    self.data[j] = self.data[self.count]
                    self.count = self.count - 1
                    self.data.pop()
                    self.swim(j)
                    self.sink(1)
                    break


    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def size(self):
        return self.count

    def GetMax(self):
        if self.count > 0:
            return self.data[1]
        else:
            return 0

    def IsContain(self, name):
        if name in self.data:
            return True
        else:
            return False

    def BuiltMAX_HEAP(self, txtfile):
        with open(txtfile, 'r') as fh:
            next(fh)
            for line in fh:
                self.count = self.count + 1
                self.data.append(line.strip())
                print("Added [", self.count, "]", self.data[self.count])
        self.i = int(self.count // 2)
        print(self.i)
        while (self.i > 0):
            self.sink(self.i)
            self.i = (self.i) - 1


    def print_MAX_HEAP(self):
        print("Printing Max PQ")
        for i in range(1, self.count + 1):
            print("[", i, "]", self.data[i])


# **************Max HEap Finished********************************
def main():
    MIN_HEAP = min_heap()
    MAX_HEAP = max_heap()
    print("Assignment 6 DEPQ Implementation")
    while (True):

        print("1>Built PQ")
        print("2> Get Max")
        print("3> Get Min")
        print("4> IsEmpty")
        print("5> IsContain")
        print("6> Size")
        print("7> Put Data")
        print("8> Remove Max")
        print("9> Remove Min")

        print("10> Print PQ")
        print("0> Exit")
        user_input = int(raw_input("Please Select an Option-->"))
        if user_input == 1:
            file_input =raw_input("Please Enter filename-->")
            MIN_HEAP.BuiltMIN_HEAP(file_input)
            MAX_HEAP.BuiltMAX_HEAP(file_input)
        elif user_input == 2:
            print(MAX_HEAP.GetMax())
        elif user_input == 3:
            print(MIN_HEAP.GetMin())
        elif user_input == 4:
            print(MIN_HEAP.isEmpty() and MAX_HEAP.isEmpty())
        elif user_input == 5:
            check_item = raw_input("Please Enter Value to Check-->")
            print(MIN_HEAP.IsContain(check_item))
        elif user_input == 6:
            if(MIN_HEAP.size()==MAX_HEAP.size()):
                print(MIN_HEAP.size())
            else:
                print(0)
        elif user_input == 7:
            put_item = raw_input("Please Enter Value to Insert-->")
            MIN_HEAP.put(put_item)
            MAX_HEAP.put(put_item)
        elif user_input == 8:
            maxout = MAX_HEAP.RemoveMax()
            print(maxout)
            MIN_HEAP.Remove(maxout)
        elif user_input == 9:
            minout = MIN_HEAP.RemoveMin()
            print(minout)
            MAX_HEAP.Remove(minout)

        elif user_input == 10:
            MIN_HEAP.print_MIN_HEAP()
            MAX_HEAP.print_MAX_HEAP()
        else:
            return 0


if __name__ == '__main__': main()
