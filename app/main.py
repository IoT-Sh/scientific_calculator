from tkinter import Tk, Frame, Button, Menu
import tkinter.messagebox
from .calc import Calc
from .display import display
from .button import button_pad

root = Tk()

root.title("Scientific Calculator")

root.configure(background = 'white')

root.resizable(width=False, height=False)

root.geometry("480x568+450+90")

calc = Frame(root)

calc.grid()

calc_value = Calc()

display(calc)

numberpad = "789456123"

i = 0

btn = []

for j in range(2, 5):
	for k in range(3):
		btn.append(Button(calc,
						width=6,
						height=2,
						bg='black',
						fg='white',
						font=('Helvetica', 20, 'bold'),
						bd=4, text=numberpad[i]))

		btn[i].grid(row=j, column=k, pady=1)

		btn[i]["command"] = lambda x=numberpad[i]: calc_value.numberEnter(x)
		i += 1

button_pad(calc, calc_value)

# use askyesno function to
# stop/continue the program execution
def iExit():
	iExit = tkinter.messagebox.askyesno("Scientific Calculator",
										"Do you want to exit ?")
	if iExit>0:
		root.destroy()
		return

def Scientific():
	root.resizable(width=False, height=False)
	root.geometry("944x568+0+0")


def Standard():
	root.resizable(width=False, height=False)
	root.geometry("480x568+0+0")

menubar = Menu(calc)

# ManuBar 1 :

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

# ManuBar 2 :

editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

root.config(menu=menubar)

root.mainloop()
