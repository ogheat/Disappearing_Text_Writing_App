from tkinter import *
from tkinter import messagebox

text = ""
new_text = ""
sec = 0
x = True

def info():
    messagebox.showinfo(title="info",message="info will be there")

def quit():
    global x
    x = False

def reset():
    email_entry.delete(1.0, END)
    email_entry.focus()

def timerupdate():
    global sec
    sec = sec + 1
    window.after(1000, timerupdate)

def timer_reset():
    global sec
    sec = 0


window = Tk()

window.title("disappearing text app")

info = Button(text="quit",command=quit,  background = 'black', foreground = "white")
info.grid(column=0,row=0)

email_label = Label(text='Type your text below',font=('courier',20,'bold'))
email_label.grid(column=1,row=0,columnspan=2)

email_entry = Text()
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(1.0,"type your text here")
email_entry.focus()


info = Button(text="info",command=info,  background = 'black', foreground = "white")
info.grid(column=3,row=0)

reset_button = Button(text="reset",command=reset,  background = 'red', foreground = "black",padx=50)
reset_button.grid(column=1,row=3,columnspan=2)


timerupdate()

while x:
    window.update_idletasks()
    window.update()
    if sec == 1:
     text = email_entry.get(1.0,END)
     email_entry['bg'] = 'white'
    elif sec == 5:
        new_text = email_entry.get(1.0,END)
        timer_reset()
        if new_text == text:
            email_entry.delete(1.0,END)
            email_entry['bg'] = 'red'











