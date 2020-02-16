def pair_sum(arr, target):
    arr.sort()
    front_index = 0
    back_index = len(arr)-1
    while front_index < back_index:
        front = arr[front_index]
        back = arr[back_index]
        if front+back == target:
            return [front, back]
        if front+back > target:
            back_index -=1
        else:
            front_index+=1
    return [None, None]
    
input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
print("Pass" if pair_sum(input_list, target) == solution else "Fail")

input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
print("Pass" if pair_sum(input_list, target) == solution else "Fail")


input_list = [110, 9, 89]
target = 9
solution = [None, None]
print("Pass" if pair_sum(input_list, target) == solution else "Fail")
