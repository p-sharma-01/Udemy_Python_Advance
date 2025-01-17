sentence="Hello I am learning python programming".split()
l=[len(i) for i in sentence]
dict={word:length for word,length in zip(sentence,l)}
print(dict)