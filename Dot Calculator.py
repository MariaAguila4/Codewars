def calculator(txt):
    # This is the place to code!
    text = txt.split(" ")
    print("text:", text)
    new = []
    sum = len(text[0]) + len(text[2])
    rest = len(text[0]) - len(text[2])
    mut = len(text[0]) * len(text[2])
    div = len(text[0]) // len(text[2])
    if (text[1] == '+'):
        lenght = sum
    elif (text[1] == '-'):
        lenght = rest
    elif (text[1] == '*'):
        lenght = mut
    elif (text[1] == '//'):
        lenght = div
    else:
        lenght = 0
    if(lenght > 0):
        for i in range(lenght):
            new.append('.')
        return "".join(new)
    else:
        return ""
    pass


print(calculator("..... + ..............."))
print("a", calculator(". - ."))