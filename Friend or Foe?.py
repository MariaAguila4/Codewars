def friend(x):
    result = []
    for i in x:
        print(i)
        if (len(i) == 4):
            result.append(i)
    return result


friends= ["Ryan", "Kieran", "Mark",]
friends = ["Ryan", "Jimmy", "123", "4", "Cool Man"]
print(friend(friends))