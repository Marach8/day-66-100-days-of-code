from tkinter import *

def update(num):
  global txt
  txt += str(num)
  label['text'] = txt
  
def equals():
  global txt
  try:
    ans = str(eval(txt))
    label['text'] = ans
    txt = ans
  except:
    label['text'] = 'Error!!!' 
    
def clear(): 
  global txt
  txt = ''
  label['text'] = ''
  
window = Tk()

window.title('GUI Basic Calc.')
window.geometry('450x450')
frame = Frame(window)
frame.place(x=40, y=0)

txt = ''

label = Label(frame, text='', height=2, width=32, bg='lightgrey')
label.grid(row=0, columnspan=4)

button = Button(frame, text='1', height=3, width=4, bg='lightblue', command=lambda:update(1))
button.grid(row=1, column=0)
button = Button(frame, text='2', height=3, width=4, bg='lightblue', command=lambda:update(2))
button.grid(row=1, column=1)
button = Button(frame, text='3', height=3, width=4, bg='lightblue', command=lambda:update(3))
button.grid(row=1, column=2)
button = Button(frame, text='+', height=3, width=4, bg='pink', command=lambda:update('+'))
button.grid(row=1, column=3)
button = Button(frame, text='4', height=3, width=4, bg='lightblue', command=lambda:update(4))
button.grid(row=2, column=0)
button = Button(frame, text='5', height=3, width=4, bg='lightblue', command=lambda:update(5))
button.grid(row=2, column=1)
button = Button(frame, text='6', height=3, width=4, bg='lightblue', command=lambda:update(6))
button.grid(row=2, column=2)
button = Button(frame, text='-', height=3, width=4, bg='pink', command=lambda:update('-'))
button.grid(row=2, column=3)
button = Button(frame, text='7', height=3, width=4,bg='lightblue', command=lambda:update(7))
button.grid(row=3, column=0)
button = Button(frame, text='8', height=3, width=4, bg='lightblue', command=lambda:update(8))
button.grid(row=3, column=1)
button = Button(frame, text='9', height=3, width=4, bg='lightblue', command=lambda:update(9))
button.grid(row=3, column=2)
button = Button(frame, text='*', height=3, width=4, bg='pink',
command=lambda:update('*'))
button.grid(row=3, column=3)
button = Button(frame, text='0', height=3, width=4, bg='lightblue', command=lambda:update(0))
button.grid(row=4, column=0)
button = Button(frame, text='.', height=3, width=4, bg='lightblue', command=lambda:update('.'))
button.grid(row=4, column=1)
button = Button(frame, text='clear', height=3, width=4, bg='red', command=lambda:clear())
button.grid(row=4, column=2)
button = Button(frame, text='/', height=3, width=4, bg='pink', command=lambda:update('/'))
button.grid(row=4, column=3)
button = Button(frame, text='=', height=3, width=28, bg='green', command=lambda:equals())
button.grid(row=5, columnspan=4)

window.mainloop()