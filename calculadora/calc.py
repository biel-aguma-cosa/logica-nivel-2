from tkinter import *

root = Tk()
root.geometry('300x380')
root.resizable(False,False)
root.columnconfigure(5)
root.rowconfigure(5)

output = Frame(root,width=300,height=45,bg='black')
output.grid(row=0,columnspan=4)
text = Label(output,fg='white',bg='black')
text.pack(side=RIGHT)

def insert(num):
    global text
    text['text'] += str(num)

_1 = Button(root,text='1',width=4,height=2,command=lambda:insert(1))
_1.grid(row=3,column=2,sticky=W,padx=10,pady=10)
_2 = Button(root,text='2',width=4,height=2)
_2.grid(row=3,column=1,sticky=W,padx=10,pady=10)
_3 = Button(root,text='3',width=4,height=2)
_3.grid(row=3,column=0,sticky=W,padx=10,pady=10)

_4 = Button(root,text='4',width=4,height=2)
_4.grid(row=2,column=2,sticky=W,padx=10,pady=10)
_5 = Button(root,text='5',width=4,height=2)
_5.grid(row=2,column=1,sticky=W,padx=10,pady=10)
_6 = Button(root,text='6',width=4,height=2)
_6.grid(row=2,column=0,sticky=W,padx=10,pady=10)

_7 = Button(root,text='7',width=4,height=2)
_7.grid(row=1,column=2,sticky=W,padx=10,pady=10)
_8 = Button(root,text='8',width=4,height=2)
_8.grid(row=1,column=1,sticky=W,padx=10,pady=10)
_9 = Button(root,text='9',width=4,height=2)
_9.grid(row=1,column=0,sticky=W,padx=10,pady=10)

root.mainloop()