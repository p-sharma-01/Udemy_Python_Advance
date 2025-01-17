import  pandas
data = pandas.read_csv("E:/GLA/udemy/comprehension/NatoAlphabet/nato_phonetic_alphabet.csv")
data.to_dict()
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
word=input("Enter a word: ").upper()
output_dict={i:phonetic_dict[i] for i in word}
output_list=[phonetic_dict[i] for i in word]
print(output_dict,output_list,sep="\n")