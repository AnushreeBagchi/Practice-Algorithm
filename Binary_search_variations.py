def binary_search_using_loop(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        middle_index = (start+end)//2
        middle_element = arr[middle_index]
        if target == middle_element:
            return middle_index
        elif target < middle_element:
            end = middle_index -1       
        elif target > middle_element:
            start = middle_index + 1        
    return -1

def find_first(arr, target):
    index = binary_search_using_loop(arr, target)
    if index == -1 :
        return -1
    while arr[index] == target:
        if index == 0:
            return 0
        if arr[index -1] == target:
            index -= 1
        else:
            return index        

arr = [1, 3, 5, 7, 7, 7, 8, 11, 12] #Find the first occurance of any repetetive number
print("Pass" if find_first(arr, 7) == 3 else "Fail")
print("Pass" if find_first(arr, 9) == -1 else "Fail")

def contains(arr, target):
    index = binary_search_using_loop(arr, target)
    if index == -1:
        return False
    else:
        return True
print("Pass" if contains(['a','b','c','d','f','h'], 'c') == True else "Fail")
print("Pass" if contains(['a','b','c','d','f','h'], 'e') == False else "Fail")

