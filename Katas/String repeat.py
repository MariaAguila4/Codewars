def repeat_str(repeat, string):
    text = []
    for i in range(repeat):
        text.append(string)
    return "".join(text)


print(repeat_str(4, 'a'))
print(repeat_str(3, 'hello '))