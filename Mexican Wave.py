def wave(people):
    print(len(people))
    text = []
    for i in range(0,len(people)):
        if(people[i] != ' '):
            word = people[:i] + people[i].upper() + people[i+1:]
            text.append(word)
    return (text)



text = "hello"
text = "two words"
text = " gap "
print(wave(text))