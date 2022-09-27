from collections import Counter
pepe = "hola"
pingu = "aalho"

def counti(sentence):
    cdict = {}
    for c in (sentence):
      if c not in cdict:
        cdict[c] = 0
      cdict[c] += 1
    return cdict

def iguals(pepe,pingu):
    print(Counter(pepe))
    print(Counter(pingu))
    if counti(pepe) == counti(pingu):
        return True
    else:
        return False

print(iguals(pepe,pingu))




sentence = "pepe"
print(counti(sentence))


