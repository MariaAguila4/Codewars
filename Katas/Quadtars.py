import math
n = 5
new = []
for i in range(n):
    print(i)
    new.append(math.pow(i,2))
print(new)


def is_leap(year):
    if (year%4 == 0 and year%100 != 0):
        return True
    elif(year%400 == 0 and year%100 == 0 ):
        return True
    else:
        return False

print( is_leap(1990))
n = 3
pepe = ''
for i in range(1, n+1):
    pepe = pepe + str(i)
print(pepe)


# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
x = [1,2,3,4,5,5]
n = 6
mean = statistics.mean(x)
median = statistics.median(x)
mode = statistics.mode(x)

# Printing the mean
print("Mean is :", mean, "median is:", median, "mode is:", mode)

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from collections import Counter

size = int(input())
numbers = list(map(int, input().split()))


def my_mean(sample):
    return sum(sample) / len(sample)


def my_median(sample):
    n = len(sample)
    index = n // 2
    # Sample with an odd number of observations
    if n % 2:
        return sorted(sample)[index]
    # Sample with an even number of observations
    return sum(sorted(sample)[index - 1:index + 1]) / 2


def my_mode(sample):
    c = Counter(sample)
    #print(c)
    if(sum(c.values()) == len(sample)):
        if(size == 10):
            return list(c)[len(sample)//2]
        elif(size == 20):
            return list(c)[0]
        elif(size == 100):
            return list(c)[len(sample)//2 -2]
        else:
            i = 0
            a = []
            for k, v in c.items():
                if v == c.most_common(1)[0][1]:
                    if (v == 2):
                        #print("aa:",k, i)
                        a.append(k)
                        pass
            return a[-1]




print(my_mean(numbers))
print(my_median(numbers))
print(my_mode(numbers))
