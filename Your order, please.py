def order(sentence):
  text = []
  sentence = sentence.split(" ")

  for i in range(1,10):
    for word in sentence:
      if str(i) in word:
        text.append(word)
  return " ".join(text)

text= "is2 Thi1s T4est 3a"
text= "4of Fo1r pe6ople g3ood th5e the2"

print(order(text))