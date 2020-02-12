# merging sorted arr
a= [1,3,5,7,9]
b= [2,4,6,8]

def merge(arr1, arr2):
    new_arr = []
    i1 = 0
    i2 = 0
    while i1 < len(arr1) and i2< len(arr2):
        if arr1[i1]<arr2[i2]:
            new_arr.append(arr1[i1])
            i1+=1
        else:
            new_arr.append(arr2[i2])
            i2+=1
    new_arr += arr1[i1:]
    new_arr += arr2[i2:]
    return new_arr

def mergesort(items):
    if len(items)<=1:
        return items
    mid = len(items)//2
    left = items[:mid]
    right = items[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

print(mergesort([21,2,5,1,67,43,41,90,56]))