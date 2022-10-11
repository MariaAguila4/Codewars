def nb_year(p0, percent, aug, p):
    index = 1
    pepe = (p0 + (p0 * percent/100) + aug)
    while pepe <= p+1:
        index +=1
        pepe =(pepe +(pepe*percent/100) + aug)
        if(pepe == p): return index
    return index

print(nb_year(1500000 ,0.0, 10000, 2000000))
print(nb_year(1000, 2, 50, 1200))
print(nb_year(1500, 5, 100, 5000))
print(nb_year(1000, 2.0, 50, 1214))