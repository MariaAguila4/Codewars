def move_zeros(lst):
    print(lst)
    new = []
    n = len(lst)
    j = 0
    zero = True
    for i in lst:
        print("i, j:", i, j)
        if (i == 0):
            print("zero trobat", lst)
            lst.append(lst.pop(lst.index(i)))
        print("list:", lst)
        j+=1
    return lst

#print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))