text = "i love you"
word = "love"

words = text.split(" ")
count = text.count(word)

frequency = count/len(words)*100
print(frequency)