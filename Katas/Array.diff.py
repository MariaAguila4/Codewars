def array_diff(a, b):
    if(len(b) == 0):
        return a

    for i in b:
        if i in a:
            for j in range(a.count(i)):
                a.remove(i)
    return a


a = [1,2,2]
b = [2]
print(array_diff(a, b))