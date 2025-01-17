import pandas
with open("E:/GLA/udemy/comprehension/compre/file1.txt") as f1:
    k=f1.readlines()
with open("E:/GLA/udemy/comprehension/compre/file2.txt") as f2:
    p=f2.readlines()
result=[int(i) for i in k if i in p]
o=pandas.DataFrame(result)
o.to_csv("Common_elements.csv")
# Write your code above this line
# Do Not Change the code below
print(result)
