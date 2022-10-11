import math
def solution(start, finish):
    dif = finish -start
    pepe = math.floor(dif / 3)
    return  pepe + dif%3




print(solution(1,5))
print(solution(2,4))