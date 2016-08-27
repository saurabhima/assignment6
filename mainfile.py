# import plotly as pt
class depq:
    def __init__(self):
        self.data = ['']
        self.count = 0

    def swim(self, index):
        while index // 2 > 0:
            child_index = index // 2
            if self.data[child_index] > self.data[index]:
                temp = self.data[index // 2]
                self.data[index // 2] = self.data[index]
                self.data[index] = temp
            index = index // 2

    def sink(self, index):
        while (index * 2) <= self.count:
            smlchild = self.smaller_child(index)
            if self.data[index] > self.data[smlchild]:
                temp = self.data[smlchild]
                self.data[smlchild] = self.data[index]
                self.data[index] = temp
            index = smlchild

    def smaller_child(self, i):
        if (i * 2 + 1) > self.count:
            return i * 2
        else:
            if self.data[i * 2] > self.data[i * 2 + 1]:
                return (i * 2 + 1)
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

    def RemoveMax(self):

        max_data = self.data.pop()
        self.count = self.count - 1
        self.swim(self.count)
        return max_data

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

    def GetMax(self):
        return self.data[self.count]

    def IsContain(self, name):
        if (name >= self.data[1] and name <= self.data[self.count]):
            return True
        else:
            return False

    def BuiltDEPQ(self, txtfile):
        fh = open(txtfile, 'r')
        next(fh)
        for f in fh.readlines():
            self.count = self.count + 1
            self.data.append(f.strip())
            self.swim(self.count)


def main():
    DEPQ = depq()
    print("Assignment 6 DEPQ Implementation")
    while (True):

        print("1>Built DEPQ")
        print("2> Get Max")
        print("3> Get Min")
        print("4> IsEmpty")
        print("5> IsContain")
        print("6> Size")
        print("7> Put Data")
        print("8> Remove Max")
        print("9> Remove Min")
        print("0> Exit")
        user_input = int(input("Please Select an Option-->"))
        if user_input == 1:
            DEPQ.BuiltDEPQ('SMALL_DATA.txt')
        elif user_input == 2:
            print(DEPQ.GetMax())
        elif user_input == 3:
            print(DEPQ.GetMin())
        elif user_input == 4:
            print(DEPQ.isEmpty())
        elif user_input == 5:
            check_item = input("Please Enter Value to Check-->")
            print(DEPQ.IsContain(check_item))
        elif user_input == 6:
            print(DEPQ.size())
        elif user_input == 7:
            put_item = input("Please Enter Value to Insert-->")
            DEPQ.put(put_item)
        elif user_input == 8:
            print(DEPQ.RemoveMax())
        elif user_input == 9:
            print(DEPQ.RemoveMin())
        else:
            return 0


if __name__ == '__main__': main()
