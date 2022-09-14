def dbl_linear2(n):
    u = [1]
    a= 0
    b =0

    while(len(u) <= n):
        y = 2 * u[a] + 1
        z = 3 *u[b] + 1
        if y > z:
            u.append(z)
            b += 1
        elif y < z:
            u.append(y)
            a += 1
        else:
            u.append(y)
            a += 1
            b += 1
    return u[n]

def dbl_linear(n) :
    list = [1]
    a = 0
    b = 0

    while(len(list)<=n) :
        y = 2*list[a] + 1
        z = 3*list[b] + 1

        if y>z :
            list.append(z)
            b+= 1
        elif y<z :
            list.append(y)
            a += 1
        else :
            list.append(y)
            a += 1
            b += 1

    return list[n]
print(dbl_linear(20))