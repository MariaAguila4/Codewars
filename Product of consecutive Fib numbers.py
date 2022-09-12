#n = int(input("value of n:"))
n = 4895
print("fibonacci Sequence:")
def fibo(n):
    first = 0
    second = 1
    suma = 0
    count = 1
    while(count <= n):
        print(suma)
        count +=1
        first = second
        second = suma
        suma = first+second
    return suma,first, second
print("fibo:",fibo(n))
def productFib(prod):
    second = 1
    suma = 0
    first = 0
    count = 1
    while(count <= prod+2):
        print(suma)
        count += 1
        first = second
        second = suma
        suma = first + second
        print("first*second",first*second, first, second, "prod",prod)

        if(first*second == prod):
            return [first, second, True]
        if(first*second > prod):
            return [first, second, False]

    return [first, second, False]
print(productFib(n))