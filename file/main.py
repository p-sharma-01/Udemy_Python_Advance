# with open("file/my_file.txt",'r') as f:
#     c=f.read()
#     print(c)
# with open("file/my_file.txt",'w') as f:
#     f.writelines("my name is pushpendra.\ni will meet u tomorrow.")

with open("file/my_new_file.txt",'a') as f:
    f.writelines("my name is pushpendra.\ni will meet u tomorrow.")
f.close()