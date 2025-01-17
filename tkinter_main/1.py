from tkinter import *
window=Tk()
window.title("My First GUI")
window.minsize(width=500,height=600)

#lebel
my_label=Label(text="",font=("Arial",24,"bold"))
my_label.pack() # side="right" or left, bottom# my_label["text"]="new label

#button
def button_click():
    my_label.config(text="label")
button=Button(text="Click me",command=button_click)
button.pack()


#   Entry
input1=Entry()
input1.pack()
input1.get()
window.mainloop()
