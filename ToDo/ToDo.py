import tkinter as tk
import webbrowser


# Colorsection for Textcolors
black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'

root = tk.Tk()
root.title("ToDo - App")
root.geometry("500x500+0+0")
root.resizable(0, 0)


def new(e):
    global a
    a = e.widget.get()
    out = tk.Label(root, text=a)
    out.place(x=80, y=150)

def timez(t):
    global b
    b = t.widget.get()
    out = tk.Label(root, text=b)
    out.place(x=80, y=170)

def descript(d):
    global c
    c = d.widget.get()
    out = tk.Label(root, text=c)
    out.place(x=80, y=190)

def savior():
    global a
    global b
    global c
    print("Saving")
    f = open("reminder.txt", "a+")
    f.write("\n-----New Entry!-----")
    f.write("\nTitle: " + a)
    f.write("\nTime: " + b)
    f.write("\nInfo: " + c)
    f.close()
    root.destroy()

def opening():
    webbrowser.open("reminder.txt")


titel = tk.Label(root, text="Title of your entry").place(x=10, y=10)
e = tk.Entry(root)
e.place(x=150, y=10)
e.bind("<Return>", new)

time = tk.Label(root, text="Enter a time here").place(x=10, y=50)
t = tk.Entry(root)
t.place(x=150, y=50)
t.bind("<Return>", timez)

details = tk.Label(root, text="More information").place(x=10, y=90)
d = tk.Entry(root)
d.place(x=150, y=90)
d.bind("<Return>", descript)

view = tk.Label(root, text="Previw of your Entry", fg="green").place(x=10, y=130)
first = tk.Label(root, text="Title: ", wraplength=40)
first.place(x=10, y=150)
second = tk.Label(root, text="Time: ")
second.place(x=10, y=170)
third = tk.Label(root, text="Description: ")
third.place(x=10, y=190)
remind = tk.Label(root, text="You need to hit \"Enter\" after every Entry or it won't work!", fg="red")
remind.place(x=10, y=230)

saver = tk.Button(root, text="SAVE", width=10, height=2, bg="gold", command=savior).place(x=245, y=400)
opener = tk.Button(root, text="OPEN", width=10, height=2, bg="blue", command=opening).place(x=145, y=400)
root.mainloop()