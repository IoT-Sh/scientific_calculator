from tkinter import Button

def num_pad(calc, val):
    numberpad = "789456123"

    i = 0

    btn = []

    for j in range(2, 5):

	    for k in range(3):
		    btn.append(Button(calc, width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'), bd=4, text=numberpad[i]))

		    btn[i].grid(row=j, column=k, pady=1)

		    btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
		    i += 1
