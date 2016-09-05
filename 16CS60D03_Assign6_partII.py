
import datetime
import os


class min_heap:
    def __init__(self):
        self.data = ['']
        self.count = 0

        self.i = 0
        self.smlchild = 0
        self.total_lines = 0

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
                if (self.data[j] == value):
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
        if (name >= self.data[1] and name <= self.data[self.count]):
            return True
        else:
            return False

    def BuiltMIN_HEAP(self, txtfile):
        fh = open(txtfile, 'r')
        # self.total_lines = int(fh.readline().strip())
        for f in fh.readlines():
            if self.count < 100:
                self.count = self.count + 1
                self.data.append(f.strip())
                # print("Added [", self.count, "]", self.data[self.count])
        fh.close()
        self.i = int(self.count // 2)
        # print(self.i)
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
        self.total_lines = 0

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
                if self.data[j] == value:
                    self.data[j] = self.data[self.count]
                    self.count = self.count - 1
                    self.data.pop()
                    self.sink(j)
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
        if (name >= self.data[1] and name <= self.data[self.count]):
            return True
        else:
            return False

    def BuiltMAX_HEAP(self, txtfile):
        fh = open(txtfile, 'r')
        # self.total_lines = int(fh.readline().strip())
        for f in fh.readlines():
            if self.count < 100:
                self.count = self.count + 1
                self.data.append(f.strip())
                # print("Added [", self.count, "]", self.data[self.count])
        fh.close()
        self.i = int(self.count // 2)
        # print(self.i)
        while (self.i > 0):
            self.sink(self.i)
            self.i = (self.i) - 1



    def print_MAX_HEAP(self):
        print("Printing Max PQ")
        for i in range(1, self.count + 1):
            print("[", i, "]", self.data[i])


# **************Max HEap Finished********************************
count_centre = 0


def recursion(file, mode, len, align):
    print("Currently Work File-->" + file + '\n')
    MIN_HEAP = min_heap()
    MAX_HEAP = max_heap()
    count_left = 0
    count_right = 0
    # file_left=''
    # file_right=''
    if mode == 0 or len > 100:
        MIN_HEAP.BuiltMIN_HEAP(file)
        MAX_HEAP.BuiltMAX_HEAP(file)
        if mode == 0:
            file_left = 'l.txt'
            file_right = 'r.txt'
            fh_left = open(file_left, 'w+')
            print("opening File-->" + file_left)
            fh_right = open(file_right, 'w+')
            print("opening File-->" + file_right)
        else:
            file_left = file.split('.txt')[0]
            file_left = file_left + 'l' + '.txt'
            file_right = file.split('.txt')[0]
            file_right = file_right + 'r' + '.txt'
            print("opening File-->" + file_left)
            fh_left = open(file_left, 'w+')
            print("opening File-->" + file_right)
            fh_right = open(file_right, 'w+')

        fh = open(file, 'r')

        count_lines = 0
        while count_lines < 100:
            fh.readline()
            count_lines = count_lines + 1
        token = False
        for f in fh.readlines():
            current_value = f.strip()
            # print(current_value)
            if current_value <= MIN_HEAP.GetMin() and current_value <= MAX_HEAP.GetMax():
                fh_left.write(f.strip() + '\n')
                count_left = count_left + 1
            elif current_value >= MAX_HEAP.GetMax() and current_value >= MIN_HEAP.GetMin():
                fh_right.write(f.strip() + '\n')
                count_right = count_right + 1
            elif current_value > MIN_HEAP.GetMin() and current_value < MAX_HEAP.GetMax():
                if token == False:
                    minout = MIN_HEAP.RemoveMin()
                    MAX_HEAP.Remove(minout)
                    fh_left.write(minout + '\n')
                    count_left = count_left + 1
                    MIN_HEAP.put(f.strip())
                    MAX_HEAP.put(f.strip())
                    token = True
                elif token == True:
                    maxout = MAX_HEAP.RemoveMax()
                    MIN_HEAP.Remove(maxout)
                    fh_right.write(maxout + '\n')
                    count_right = count_right + 1
                    MIN_HEAP.put(f.strip())
                    MAX_HEAP.put(f.strip())
                    token = False

        MIN_HEAP.data.sort()

    if mode == 0:
        centre_file = 'c.txt'
    else:
        centre_file = 'c' + file.split('.txt')[0] + '.txt'
    fh_centre = open(centre_file, 'w+')
    # fh_centre.write(str(MIN_HEAP.count))
    if (count_left < 100):
        fh_left.close()
        left_list = []
        fh_left = open(file_left, 'r')
        for line in fh_left.readlines():
            left_list.append(line.strip())
        left_list.sort()
        for item in left_list:
            fh_centre.write(item + '\n')

    print("Opening FIle-->" + centre_file)
    global count_centre
    count_centre = count_centre + 1
    for a in range(1, MIN_HEAP.count + 1):
        fh_centre.write(MIN_HEAP.data[a].strip() + '\n')
    if (count_right < 100):
        fh_right.close()
        right_list = []
        fh_right = open(file_right, 'r')
        for line in fh_right.readlines():
            right_list.append(line.strip())
        right_list.sort()
        for item in right_list:
            fh_centre.write(item + '\n')

    fh_centre.close()
    fh.close()
    fh_left.close()
    fh_right.close()
    if count_right >= 100:
        recursion(file_right, 1, count_right, 1)
    if count_left >= 100:
        recursion(file_left, 1, count_left, -1)

    return (count_centre)

def write_data_sub(filename):
    fh_write = open('final_output.txt', 'a+')
    centre_file = filename
    fh = open(centre_file, 'r')
    print("currently COpy File--> " + centre_file)
    for line in fh.readlines():
        fh_write.write(line.strip() + '\n')
    fh.close()
    fh_write.close()


def write_data(filename):

    centre_file=filename
    left_file=filename.split('.txt')[0]
    right_file=filename.split('.txt')[0]
    left_file=left_file+'l'+'.txt'
    right_file = right_file + 'r' + '.txt'
    if (os.path.isfile(left_file)):
        write_data(left_file)
    write_data_sub(centre_file)

    if (os.path.isfile(right_file)):
        write_data(right_file)



    # filename_new = filename.split('.txt')[0]
    # count = count + 1
    # if count > 20:
    #     return
    # filename_new = filename_new[0:-1]
    # filename_new = filename_new + '.txt'
    # if (os.path.isfile(filename_new)):
    #     write_data(filename_new)
    #     filename_new = filename.split('.txt')[0]
    #     filename_new = filename_new + 'r'
    #     filename_new = filename_new + '.txt'
    #     if (os.path.isfile(filename_new)):
    #         write_data(filename_new)


def main():
    print("Assignment 6 DEPQ Implementation Part II")

    file_input = raw_input("Please Enter filename-->")
    file_handle = open(file_input, 'r')
    cwd = os.getcwd()
    print(cwd)
    newdir = cwd + '/proj_data'
    if os.path.isdir(newdir) == False:
        os.mkdir(newdir)
    os.chdir(newdir)
    temp_file_handle = open('temp_input_file.txt', 'w')
    line_count = int(file_handle.readline())
    for fh in file_handle.readlines():
        temp_file_handle.write(fh.strip() + '\n')
    temp_file_handle.close()
    file_handle.close()
    total_sub_set = recursion('temp_input_file.txt', 0, line_count, 0)
    centre_file_check = 'c.txt'
    left_ptr = -1
    centre_left_prev = ''
    while (os.path.isfile(centre_file_check)):
        # print(centre_file_check +" exist")
        centre_left_prev = centre_file_check
        left_ptr = left_ptr + 1
        centre_file_check = centre_file_check.split('.txt')[0]
        centre_file_check = centre_file_check + 'l' + '.txt'

    centre_file_check = centre_left_prev
    write_data('c.txt')

    return 0


if __name__ == '__main__': main()
