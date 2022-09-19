def m(k):
    return(k%2 )== 0
print(m(3))

def f(ht):
    b= 0
    for elt in ht:
        b= elt + b
    return b
text = [1,2,3,1]
print(f(text))

m = 0.01
n = 0.5
def s(m,n):
    r= None
    if m <= n:
        r = m
    else:
        r = n
    return r
print(s(m,n))


def interes_anual(cantidad, interes):
    return cantidad * (1 + interes / 100)

def retorno_inversion(cantidad, interes, anyos):
    r = []
    for anyos in range(anyos):
        cantidad = interes_anual(cantidad, interes)
        r.append (round( cantidad, 2))
    return r


cantidad= 10
interes=4
anyos=3
print(retorno_inversion(cantidad, interes, anyos))
#.-------------

def applyToEachString(stringFunction, *words):
    myList = []
    for word in words:
        myList.append(stringFunction(word))
    return tuple(myList)


def onlyVowels(word):
    vowels = 'aeiouáéíóúu'
    resp = ""
    for letter in word:
        if letter in vowels or letter in vowels:
            resp = resp + letter
    return resp

print(applyToEachString(onlyVowels, "Periódico", "Navío", "Computadora"))#("eióio", "aío", "ouaoa")

####

def applyToEachString(stringFunction, *words):
    myList = []
    for word in words:
        myList.append(stringFunction(word))
    return tuple(myList)

print(applyToEachString(str.upper,"Periodico", "navío", "computadora"))

def what_i_do(p1, p2):
    if p2 < len(p1):
        return p1
    gap = (p2 - len(p1)) // 2

    return " " * gap + p1
print(what_i_do('hola',50))

########
def second_scored(*lis):
    maximum = max(lis)
    preMax = min(lis)
    print(maximum, preMax)
    for nombre in lis:
        if (nombre < maximum and nombre > preMax):
            preMax = nombre
    return preMax

def another_second_scored(*lis):
    arr = list(set(lis))
    arr.sort()
    return arr [-2]

def other_second_scored(*lis):
    for n in lis:
        i = 2
        is_second = True
        while i <= n // 2:
            if n % i== 0:
                is_second = False
            i +=1
        if is_second:
            return n

def the_second_scored(*lis):
    first = max(lis)
    lis = list(lis)
    lis.remove(first)
    while first == max(lis):
        lis.remove(first)
    return max(lis)
lists = 6
lo = 8
li= 1
pepe= 4
print("second_scored:", second_scored(lists,lo,li,pepe))
print("another_second_scored(*lis)", another_second_scored(lists,lo,li,pepe))
print("other_second_scored(*lis)", other_second_scored(lists,lo,li,pepe))
print("the_second_scored", the_second_scored(lists,lo,li,pepe))

def n(a):
    return (a%2) == 0
def p(k):
    return not n(k)
print(p(1))

def g(xxs):
    k= 1
    for elm in xxs:
        k = k*elm
    return k
print(g([1,2,4]))

for x in ['Darth', 'luke','obi']:
    print(x)
    pass
for x in range(0,6):
    print("index:", x)
    pass
print(x)
index = 0
while index <= 6:
    print("i:",index)
    pass
    index = index +1
print(index)

for x in range (0,9):
    print("i:", x)
    pass

lista = [1,2,3,4,5,6,7,8,9]


multiplied_list = [element * 2 for element in lista]
print(multiplied_list)

b = 42
def f1(b,k):
    return b+k
print(f1(0,8))

q = 51
def np(a):
    #print("q1:",q)
    q=42
    print("q2:",q)
    return q*a
print(np(123))

z = -9
def ik(z):
    return z
print(ik(42))

fruits = {'banana', 'apple', 'oranges','cherry'}
print(type(fruits))
fruits.add('orange')
print(fruits)

def adder(n):
    return lambda x: x + n
a = adder(2)
print("aaa",a(8))

def f (*args):
    return 3
def g(f):
    def k(*args):
        return 2* f(*args)
    return k
a = g(f)
print(a(1,2))

class Star:
    def __init__(self,name):
        self.name = name
class Jedi (Star):
    def __init__(self,name, midi):
        super().__init__(name)
        self.midi = midi

cha = [Jedi('Ana', 100), Jedi('Yoda', 10)]
sum = 0
for elt in cha:
    sum = sum +elt.midi
print(sum)
