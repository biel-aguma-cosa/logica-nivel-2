from tkinter import *
from tkinter import font

root = Tk()
root.geometry('480x360')
root.resizable(False,False)
root.title('Quantidade de Votos')
root.configure(bg='white')

title = Label(text='Insira as informações necessárias:',width=40,bg='green',fg='white',font=("Arial",16,"italic"))
title.pack(side=TOP)

input_box = Frame(bg='yellow',height=100,width=250)
input_box.pack(side=LEFT,fill=Y)

graph_n = 0
graph_b = 0
graph_v = 0
def do_math(output=False):
    global graph_n
    global graph_b
    global graph_v
    try:
        x = int(null_in.get())
        y = int(blank_in.get())
        z = int(valid_in.get())
        total = x+y+z
        graph_n = (x*100)/total
        graph_b = (y*100)/total
        graph_v = (z*100)/total
        result['text'] = 'N: '+str(graph_n)[:2]+'% | B: '+str(graph_b)[:2]+'% | V: '+str(graph_v)[:2]+'%'
        result['fg'] = 'black'
        if output:
            return [x,y,z]
    except:
        result['text'] = 'ERRO'
        result['fg'] = 'red'


null_txt = Label(input_box,text='Votos Nulos:',bg='yellow')
null_txt.grid(row=1,column=0,padx=6,pady=25)
null_in = Entry(input_box)
null_in.grid(row=1,column=1,padx=8,pady=25)
blank_txt = Label(input_box,text='Votos Brancos:',bg='yellow')
blank_txt.grid(row=2,column=0,padx=6,pady=25)
blank_in = Entry(input_box)
blank_in.grid(row=2,column=1,padx=8,pady=25)
valid_txt = Label(input_box,text='Votos Validos:',bg='yellow')
valid_txt.grid(row=3,column=0,padx=6,pady=25)
valid_in = Entry(input_box)
valid_in.grid(row=3,column=1,padx=8,pady=25)

calculate = Button(input_box,text='Calcular Porcentagem',command=do_math)
calculate.grid(row=4,columnspan=2,padx=15,pady=25)
result = Label(input_box,text='N: X% | B: Y% | V: Z%',bg='yellow',font=('Arial',12,'roman','bold'))
result.grid(row=0,columnspan=2,padx=15,pady=10)

canvas_box = Frame(root)
canvas_box.pack(side=RIGHT,padx=20)
canvas_text = Label(canvas_box,text='Gráfico:',)
canvas_text.grid(row=0,column=0)
result_canvas = Canvas(canvas_box,width=200,height=200)
result_canvas.grid(row=1,column=0)

root.mainloop()
