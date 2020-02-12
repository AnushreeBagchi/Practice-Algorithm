input = "fedRTSersUXJ"

def string_sort(string):
    arr = list()
    for char in string:
        arr.append(ord(char))
    arr = mergesort(arr)
    output = ""
    for element in arr:
        output += chr(element)
    return output


def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def merge(arr1, arr2):
    new_arr = list()
    counter1 = 0
    counter2 = 0
    while counter1 < len(arr1) and counter2 < len(arr2):
        if arr1[counter1] < arr2[counter2]:
            new_arr.append(arr1[counter1])
            counter1+=1
        else:
            new_arr.append(arr2[counter2])
            counter2+=1
    new_arr += arr1[counter1:]
    new_arr += arr2[counter2:]
    return new_arr


def sort(input_string):
    lower = ''
    upper= ''
    output = ''
    for char in input_string:
        if ord(char) >=97 :
            lower += char
        else:
            upper += char
    lower = string_sort(lower)
    upper = string_sort(upper)  
    lower_counter = 0
    upper_counter = 0 
    for char in   input_string:
        if ord(char) > 97:
            output+= lower[lower_counter]
            lower_counter+=1
        else:
            output+= upper[upper_counter]
            upper_counter+=1
    return output

print("Pass" if sort("fedRTSersUXJ") == "deeJRSfrsTUX" else "Fail")
print("Pass" if sort("defRTSersUXI") == "deeIRSfrsTUX" else "Fail")
