def likes(names):
    if(len(names) > 3):
        return (names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this')
    if (len(names) == 1):
        return (names[0] + ' likes this')
    elif (len(names) == 2):
        return (names[0] + ' and ' + names[1] + ' like this')
    elif (len(names) == 3):
        return ( names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this')
    else:
        return 'no one likes this'



print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))