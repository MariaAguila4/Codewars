import math
def movie(card, ticket, perc):
    b = card
    i = 1
    while True:
        a = ticket*i
        b += (ticket*perc**i)
        if (math.ceil(b) < a):
            return i
        i+=1


print(movie(500, 15, 0.9))
print(movie(100, 10, 0.95))