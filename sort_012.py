def sort_012(arr):
    next_pos_0 = 0
    next_pos_2 = len(arr)-1
    front_index = 0
    while front_index < next_pos_2:
        if arr[front_index] == 0:
            arr[front_index] = arr[next_pos_0]
            arr[next_pos_0] = 0
            next_pos_0+=1
            front_index+=1
        elif arr[front_index] == 2:
            arr[front_index] = arr[next_pos_2]
            arr[next_pos_2] = 2
            next_pos_2 -=1
        else:
            front_index +=1

arr = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
sort_012(arr)
print(arr)

