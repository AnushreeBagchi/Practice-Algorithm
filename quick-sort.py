def quick_sort(items):
    sort_all(items, 0, len(items)-1)

def sort_all(items, begin_index, end_index):
    if begin_index > end_index:
        return
    pivot_index = sort_a_little(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index-1)
    sort_all(items, pivot_index+1, end_index)

def sort_a_little(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]
    while left_index != pivot_index:
        item = items[left_index]
        if item < pivot_value:
            left_index += 1
            continue
        else:
            items[left_index]= items[pivot_index-1]
            items[pivot_index-1] = items[pivot_index]
            items[pivot_index] = item
            pivot_index -=1
    return pivot_index


items = [8, 3, 1, 7, 0, 10, 2]
quick_sort(items)
print("Pass" if items == [0,1,2,3,7,8,10] else "Fail")

items = [1, 0]
quick_sort(items)
print("Pass" if items == [0,1] else "Fail")

items = [96, 97, 98]
quick_sort(items)
print("Pass" if items == [96,97,98] else "Fail")