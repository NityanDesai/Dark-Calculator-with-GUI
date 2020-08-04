from tkinter import *
root = Tk()
root.geometry("344x600")
root.title('Dark Calculator')
root.wm_iconbitmap('1.ico')
root.configure(background='grey20')
# root.overrideredirect(True) #Turns off the titlebar

scvalue = StringVar()
scvalue.set('')
screen = Entry(root, insertbackground='white', textvar=scvalue, font='futura 30 bold', bg='grey10', fg='white')
screen.pack(fill=X, ipadx=8, padx=10, pady=10)

def click(event):
    global scvalue
    text = event.widget.cget('text')
    # print(text)
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = 'ERROR'
                screen.update()
        scvalue.set(value)
        screen.update()
    elif text == 'C':
        scvalue.set('')
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

num = 9
for i in range(3):
    f = Frame(root, bg='grey16')
    for j in range(3):
        b = Button(f, text=str(num), padx=12, pady=5, font='futura 20', bg='grey40', fg='white')
        b.pack(side=LEFT, padx=12, pady=5)
        b.bind('<Button-1>', click)
        num = num - 1
    f.pack()

f = Frame(root, bg='grey16')
b = Button(f, text='.', padx=16, pady=5, font='futura 18', bg='grey40', fg='white')
b.pack(side=LEFT, padx=13, pady=5)
b.bind('<Button-1>', click)
b = Button(f, text='0', padx=10, pady=3, font='futura 20', bg='grey40', fg='white')
b.pack(side=LEFT, padx=13, pady=5)
b.bind('<Button-1>', click)
b = Button(f, text='00', padx=11, pady=9, font='futura 15', bg='grey40', fg='white')
b.pack(side=LEFT, padx=13, pady=5)
b.bind('<Button-1>', click)
f.pack()

f = Frame(root, bg='grey16')
b = Button(f, text='+', padx=13, pady=5, font='futura 16', bg='grey25', fg='white')
b.pack(side=LEFT, padx=13, pady=5)
b.bind('<Button-1>', click)
b = Button(f, text='-', padx=13, pady=5, font='futura 17', bg='grey25', fg='white')
b.pack(side=LEFT, padx=13, pady=5)
b.bind('<Button-1>', click)
b = Button(f, text='%', padx=13, pady=5, font='futura 16', bg='grey25', fg='white')
b.pack(side=LEFT, padx=13, pady=5)
b.bind('<Button-1>', click)
f.pack()

f = Frame(root, bg='grey16')
b = Button(f, text='*', padx=13, pady=5, font='futura 20', bg='grey25', fg='white')
b.pack(side=LEFT, padx=13, pady=5)
b.bind('<Button-1>', click)
b = Button(f, text='/', padx=12, pady=5, font='futura 20', bg='grey25', fg='white')
b.pack(side=LEFT, padx=12, pady=5)
b.bind('<Button-1>', click)
b = Button(f, text='C', padx=13, pady=5, font='futura 20', bg='firebrick1', fg='white')
b.pack(side=LEFT, padx=13, pady=5)
b.bind('<Button-1>', click)
f.pack()

f = Frame(root, bg='grey16')
b = Button(f, text='=', padx=99, pady=5, font='futura 20', bg='lime green', fg='white')
b.pack(side=LEFT, padx=12, pady=5, fill=X)
b.bind('<Button-1>', click)
f.pack()

root.mainloop()