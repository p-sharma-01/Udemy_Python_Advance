from tkinter import *
window=Tk()
window.minsize(height=600,width=500)
def over_write():
    new_text=input1.get()
    label1.config(text=new_text)

label1=Label(font=("Arial",24,"bold"))
label1.grid(column=0,row=0)


button=Button(text="Click me",command="over_write")
button.grid(column=1,row=1)

# Entry
input1=Entry()
input1.grid(column=3,row=1)


window.mainloop()