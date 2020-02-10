class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0
    def insert(self, data):
        self.cbt[self.next_index] = data
        self.up_heapify()
        self.next_index+=1
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2*len(self.cbt))]
            for index in range(self.next_index):
                self.cbt[index] = temp[index]
        return self.cbt

    def up_heapify(self):
        child_index = self.next_index        
        while child_index >= 1:
            parent_index = (child_index-1)//2
            child_element = self.cbt[child_index]
            parent_element = self.cbt[parent_index]
            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element
                child_index = parent_index
            else:
                break
    
    def size(self):
        return self.next_index
    def remove(self):
        if self.size()==0:
            return None
        self.next_index -=1
        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        self.cbt[0] == last_element
        self.cbt[self.next_index] = to_remove

        self.down_heapify()
        return to_remove

    def down_heapify(self):
        parent_index = 0
        while parent_index < self.next_index:
            left_child_index = 2*parent_index+1
            right_child_index = 2*parent_index+2
            parent = self.cbt[parent_index]
            left_child = None
            right_child = None
            min_elem = parent
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]
            if left_child is not None:
                min_elem = min(parent, left_child)
            if right_child is not None:
                min_elem = min(min_elem, right_child)
            if min_elem == parent:
                return
            if min_elem == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_elem
                parent = left_child_index
            if min_elem == right_child:
                self.cbt[right_child_index] =  parent
                self.cbt[parent_index] = min_elem
                parent = right_child_index
    
    def to_list(self):
        py_list = list()
        for elem in self.cbt:
            py_list.append(elem)
        return py_list

heap = Heap(5)
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(15)
heap.insert(25)
print(heap.to_list())
print(heap.remove())
print(heap.to_list())



