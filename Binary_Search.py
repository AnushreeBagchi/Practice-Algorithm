# Given a sorted array of integers, and a target value, find the index of the target value in the array. 
# If the target value is not present in the array, return -1.

# Iterative soluton
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

arr = [0,1,2,3,4,5,6,7,8,9]
print("Pass" if binary_search_using_loop(arr, 5) == 5 else "Fail")
print("Pass" if binary_search_using_loop(arr, 10) == -1 else "Fail")

#Recursive solution
def binary_search_using_recursion(arr, target):
    return return_binary_search(arr, target, 0, len(arr)-1 )

def return_binary_search(arr, target, start, end):
    if start <= end:
        middle_index = (start+end)//2
        middle_element = arr[middle_index]
        if target == middle_element:
            return middle_index
        else:
            if target < middle_element:
                end = middle_index-1                
            elif target > middle_element:
                start = middle_index +1
            return return_binary_search(arr, target, start, end)
    else:
        return -1

print("Pass" if binary_search_using_recursion(arr, 10)== -1 else "Fail")
print("Pass" if binary_search_using_recursion(arr, 4)== 4 else "Fail")
