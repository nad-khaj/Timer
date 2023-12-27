import time
import timeit
from tkinter import *
import messagebox
from time import sleep
def btnClick(s):
    global operator
    operator += str(s)
    text_input.set(operator)
def btnClear():
    global operator,counter
    operator = ""
    counter = 0
    text_input.set(operator)
def format_time(seconds):
    time_str = time.gmtime(seconds)
    formatted_time = time.strftime("%H:%M:%S",time_str)
    return formatted_time
def btnStart():
    global operator, counter
    timeval = int(operator)
    if timeval <=0:
        return
    timeval-=1
    counter+=1
    operator = str(timeval)
    timer1 = format_time(timeval)
    timer2 = format_time(counter)
    entry.get()
    entry.delete(0, END)
    entry.insert(END,timer1+" "*10+ timer2)
    entry.after(1000, btnStart)
operator = ""
win =Tk()
win.geometry("410x380")
win.title = "Timer"
win.resizable(None,None)
win.iconbitmap("image/timer.ico")
win.configure(bg="light gray" )
text_input = StringVar()
entry = Entry(win,width = 20,  font=('arial',25, 'bold'),bd=25,bg='powder blue',textvariable=text_input)
entry.grid(columnspan=4)
btn1 = Button(win, padx=5, pady=5, bd=10 ,bg= '#eff3f6', fg='black', font=('arial', 25, 'bold'),
               text='1', command=lambda:btnClick(1)).grid(row=1, column=0)
btn2 = Button(win, padx=5, pady=5, bd=10,bg= '#eff3f6' , fg='black', font=('arial', 25, 'bold'),
               text='2', command=lambda:btnClick(2)).grid(row=1, column=1)
btn3 = Button(win, padx=5, pady=5, bd=10,bg= '#eff3f6',fg='black', font=('arial', 25, 'bold'),
               text='3', command=lambda:btnClick(3)).grid(row=1, column=2)
btn4 = Button(win,padx= 5,pady = 5, bd=10,bg= '#eff3f6',fg='black', font=('arial', 25, 'bold'),
               text='4', command=lambda:btnClick(4)).grid(row=1, column=3)
btn5 = Button(win,padx= 5,pady = 5, bd=10,bg= '#eff3f6',fg='black', font=('arial', 25, 'bold'),
               text='5', command=lambda:btnClick(5)).grid(row=2, column=0)
btn6 = Button(win,padx= 5,pady = 5, bd=10,bg= '#eff3f6',fg='black', font=('arial', 25, 'bold'),
               text='6', command=lambda:btnClick(6)).grid(row=2, column=1)
btn7 = Button(win,padx=5,pady=5, bd=10,bg= '#eff3f6',fg='black', font=('arial', 25, 'bold'),
               text='7', command=lambda:btnClick(7)).grid(row=2, column=2)
btn8 = Button(win,padx=5,pady=5, bd=10,bg= '#eff3f6',fg='black', font=('arial', 25, 'bold'),
               text='8', command=lambda:btnClick(8)).grid(row=2, column=3)
btn9 = Button(win,padx=5,pady=5, bd=10,bg= '#eff3f6',fg='black', font=('arial', 25, 'bold'),
               text='9', command=lambda:btnClick(9)).grid(row=3, column=0)
btn0 = Button(win, padx=5, pady=5, bd=10,bg= '#eff3f6', fg='black', font=('arial', 25, 'bold'),
               text='0', command=lambda:btnClick(0)).grid(row=3, column=1)
btnst = Button(win, padx=5, pady=5, bd=10,bg= '#eff3f6', fg='red', font=('arial', 25, 'bold'),
               text='»', command=btnStart).grid(row=3, column=3)
btnclr = Button(win, padx=5, pady=5, bd=10,bg= '#eff3f6' , fg='red', font=('arial', 25, 'bold'),
               text='C',command = btnClear).grid(row=3, column=2)
counter = 0

# btn.bind("<Button-1>",pass)
win.mainloop()
