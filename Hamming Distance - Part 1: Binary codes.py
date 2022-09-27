def hamming_distance(a, b):
    dif = 0
    for i in range(len(a)):
        if(a[i] != b[i]):
            dif += 1
    return dif


print(hamming_distance('100101', '101001'))
print(hamming_distance('1010', '0101'))