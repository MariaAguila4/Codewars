def bubblesort_once(l):
    ar = l[::]
    for i in range(len(ar)-1):
        if ar[i] > ar[i+1]:
            ar[i], ar[i+1] = ar[i+1], ar[i]
    return ar


print(bubblesort_once([9, 7, 5, 3, 1, 2, 4, 6, 8]))