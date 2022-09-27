def modify_multiply(st, loc, num):
    text = st.split(" ")
    texts = []
    for i in range(num):
        texts.append(text[loc])
    return "-".join(texts)


print(modify_multiply("This is a string",3 ,5))
print(modify_multiply("Creativity is the process of having original ideas that have value. It is a process; it's not random.",8 ,10))