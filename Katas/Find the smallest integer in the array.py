def find_smallest_int(arr):
    arr.sort()
    return arr[0]

print(find_smallest_int([78, 56, 232, 12, 11, 43]))