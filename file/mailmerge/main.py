placeholder='[name]'
with open("./file/mailmerge/input/Names/to_names.txt",'r') as names:
    k=names.readlines()
with open("./file/mailmerge/input/Letters/starting_letter.txt",'r') as f:
        c=f.read()
        for name in k:
            s=c.replace(placeholder,name.strip())
            with open(f"./file/mailmerge/output/ReadyToSend/letter_to_{name.strip()}.txt",'w') as wr:
                 wr.write(s)

    
    
