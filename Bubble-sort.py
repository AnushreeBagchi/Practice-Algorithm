def bubble_sort1(arr):
    sort = True
    while sort:
        sort = False
        for i in range(len(arr)):        
            if i+1 < len(arr) and arr[i] > arr[i+1]:
                sort = True
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr
wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
print("Pass" if bubble_sort1(wakeup_times)[0] == 3 else "Fail")

def bubble_sort_2(arr):
    sort = True
    while sort:
        sort = False
        for i in range(len(arr)):
            if i-1 >= 0:
                this = arr[i]
                prev = arr[i-1]
                if (this[0] > prev[0]) or (this[0] == prev[0] and this[1] > prev[1]):
                    sort = True
                    temp = arr[i]
                    arr[i] = arr[i-1]
                    arr[i-1] = temp
    return arr
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]
bubble_sort_2(sleep_times)
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")