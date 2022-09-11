
def duplicate_count(text):
    result = {}
    repe= 0
    text=text.lower()
    for char in set(text):
        result[char]=text.count(char)
        if(result[char] > 1):
            repe +=1
    return repe

texts = "abcde"
texts= "abcdeaa"
texts= "abcdeaB"
texts= "Indivisibilities"
print(duplicate_count(texts))
