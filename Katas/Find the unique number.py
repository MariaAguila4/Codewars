
def find_uniq(arr):
    for i in set(arr):
        if arr.count(i) == 1:
            return i


print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))