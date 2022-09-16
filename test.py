def m(k):
    return(k%2 )== 0
print(m(3))

def f(ht):
    b= 0
    for elt in ht:
        b= elt + b
    return b
text = [1,2,3]
print(f(text))