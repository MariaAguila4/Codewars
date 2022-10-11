def xo(s):
    s.lower()
    x = 0
    o = 0
    for i in s:
        if i == 'x':
            x += 1
        if i == 'o':
            o += 1
    if (x == o):
        return True
    else:
        return False

print(xo('xo'))
print(xo('xo0'))
print( xo('xxxoo'))


def digitize(n):
    pepe = []
    for i in (str(n)):
        pepe.append(int(i))
    pepe.reverse()
    return pepe

print(digitize(35231))