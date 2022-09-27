from collections import Counter

def count(string):
    string.lower()
    freq_count = Counter(string)
    new = str(freq_count).split("(")
    a = new[1].replace(")", "")

    print(type(freq_count))
    return a

print(count('aba'))