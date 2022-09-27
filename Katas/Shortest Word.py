def find_short(s):
    x = s.split(" ")
    lenght = []
    for i in x:
        lenght.append(len(i))
    lenght.sort()
    return lenght[0]
    #return l # l: shortest word length


text= "bitcoin take over the world maybe who knows perhaps"
text= "turns out random test cases are easier than writing out basic ones"
text= "i want to travel the world writing code one day"
print(find_short(text))