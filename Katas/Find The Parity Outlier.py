def find_outlier(integers):
    even = []
    odd= []
    for i in integers:
        if (i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    if len(even) < len(odd):
        return even
    else:
        return odd


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))