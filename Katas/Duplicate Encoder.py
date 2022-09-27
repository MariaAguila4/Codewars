from collections import Counter

def duplicate_encode_NoXutaBE(string):
    string = string.lower()
    text = string
    print("text:", text)
    freq_count = Counter(string)  # get dictionary with letters as key and frequency as value
    print(freq_count)
    for key in freq_count.keys():
        if key != ")" or key != "(":
            if freq_count.get(key) < 1:  # for all different keys, list the letters and frequencies
                print("(" + key + ", " + str(freq_count.get(key)) + ")")
                text = text.replace(key, "(")
                print("req_count.get(key) > 1:", text)
            else:
                text = text.replace(key, ")")
                print("req_count.get(key) < 1:", text)
        else:
            continue

    print("final", text)
    return text
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

text = "din"
text = "recede"
text = "Success"
text = "(( @"
text = "  ( ( )"
print(duplicate_encode(text))
print(duplicate_encode_NoXutaBE(text))