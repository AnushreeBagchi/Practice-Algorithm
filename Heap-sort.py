class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0
    def insert(self, data):
        self.cbt[self.next_index] = data
        self.up_heapify()
        self.next_index +=1
        if self.next_index > len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2*len(self.cbt))]
            for index in range(self.next_index):
                self.cbt[index] = temp[index]
    def up_heapify(self):
        child_index = self.next_index
        while child_index > 0:
            child_value = self.cbt[child_index]
            parent_index = child_index//2
            parent_value = self.cbt[parent_index]
            if child_value < parent_value:
                break
            else:
                self.cbt[parent_index] = child_value
                self.cbt[child_index] = parent_value
                child_index = parent_index
    def to_list(self):
        return self.cbt
    def size(self):
        return len(self.cbt)
    def remove(self):
        to_remove = self.cbt[0]
        if self.size() == 0:
            return
        self.next_index -= 1
        last_element = self.cbt[self.next_index]
        self.cbt[self.next_index] = to_remove
        self.cbt[0] = last_element

        self.down_heapify()
    def down_heapify(self):
        parent_index = 0
        while parent_index < self.next_index:
            parent_value = self.cbt[parent_index]
            left_value = None
            right_value = None
            max_value = parent_value
            left_index = 2*parent_index+1
            right_index = 2*parent_index+2

            if left_index < self.next_index:
                left_value = self.cbt[left_index]
            
            if right_index < self.next_index:
                right_value = self.cbt[right_index]
           
            
            if left_value is not None:
                max_value = max(parent_value, left_value)
            if right_value is not None:
                max_value = max(right_value, max_value)
            if max_value == parent_value:
                return 
            if max_value == left_value:
                self.cbt[parent_index] = left_value
                self.cbt[left_index] = parent_value
                parent_index = left_index
            if max_value == right_value:
                self.cbt[parent_index] = right_value
                self.cbt[right_index] = parent_value
                parent_index = right_index
            
def heapsort(arr):
    length = len(arr)
    heap = Heap(length)
    for i in arr:
        heap.insert(i)
    for i in range(length):
        heap.remove()
    return heap.to_list()

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
print("Pass" if heapsort(arr) == [3,3,3,4,4,4,4,5,5,5] else "Fail")

arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
print("Pass" if heapsort(arr) == [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9] else "Fail")

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
print("Pass" if heapsort(arr) == solution else "Fail")

arr = [99]
solution = [99]
print("Pass" if heapsort(arr) == solution else "Fail")


arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
print("Pass" if heapsort(arr) == solution else "Fail")




