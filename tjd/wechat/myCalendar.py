import calendar

cal=calendar.month(2016,7)
print("2016年7月的日历：")
print(cal)

def myFunction(str):
    print(str);
    return;

myFunction("呵呵")

name=['a','b']
name=[0]


from tkinter import *

canvas = Canvas(width=800, height=600, bg='yellow')
canvas.pack(expand=YES, fill=BOTH)
k = 1
j = 1
for i in range(0,26):
    canvas.create_oval(400,400 - k,5,5, width=1)
    k += j
    j += 0.3

mainloop()


