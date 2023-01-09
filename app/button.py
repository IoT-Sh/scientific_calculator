from tkinter import Button, Label, CENTER

def button_pad(calc, added_value):

    btnClear = Button(calc, text=chr(67),
				width=6, height=2,
				bg='powder blue',
				font=('Helvetica', 20, 'bold'),
				bd=4,
				command=added_value.Clear_Entry).grid(
	    row=1, column=0, pady=1)

    btnAllClear = Button(calc, text=chr(67)+chr(69),
					width=6, height=2,
					bg='powder blue',
					font=('Helvetica',
						20, 'bold'), bd=4,
					command=added_value.All_Clear_Entry).grid(
	row=1, column=1, pady=1)

    btnsq = Button(calc, text="\u221A", width=6,
			height=2, bg='powder blue',
			font=('Helvetica', 20, 'bold'),
			bd=4, command=added_value.squared).grid(
	    row=1, column=2, pady=1)

    btnAdd = Button(calc, text="+", width=6,
				height=2, bg='powder blue',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=lambda: added_value.operation("add")
				).grid(row=1, column=3, pady=1)

    btnSub = Button(calc, text="-", width=6,
				height=2, bg='powder blue',
				font=('Helvetica', 20, 'bold'),
				bd=4,
				command=lambda: added_value.operation("sub")
				).grid(row=2, column=3, pady=1)

    btnMul = Button(calc, text="x", width=6, height=2,
				bg='powder blue',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=lambda: added_value.operation("multi")
				).grid(row=3, column=3, pady=1)

    btnDiv = Button(calc, text="/", width=6,
				height=2, bg='powder blue',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=lambda: added_value.operation("divide")
				).grid(row=4, column=3, pady=1)

    btnZero = Button(calc, text="0", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=lambda: added_value.numberEnter(0)
				).grid(row=5, column=0, pady=1)

    btnDot = Button(calc, text=".", width=6,
				height=2, bg='powder blue',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=lambda: added_value.numberEnter(".")
				).grid(row=5, column=1, pady=1)
    btnPM = Button(calc, text=chr(177), width=6,
			height=2, bg='powder blue',
			font=('Helvetica', 20, 'bold'),
			bd=4, command=added_value.mathPM
			).grid(row=5, column=2, pady=1)

    btnEquals = Button(calc, text="=", width=6,
				height=2, bg='powder blue',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.sum_of_total
				).grid(row=5, column=3, pady=1)
# ROW 1 :

    btnPi = Button(calc, text="pi", width=6,
			height=2, bg='black', fg='white',
			font=('Helvetica', 20, 'bold'),
			bd=4, command=added_value.pi
			).grid(row=1, column=4, pady=1)

    btnCos = Button(calc, text="Cos", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.cos
				).grid(row=1, column=5, pady=1)

    btntan = Button(calc, text="tan", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.tan
				).grid(row=1, column=6, pady=1)

    btnsin = Button(calc, text="sin", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.sin
				).grid(row=1, column=7, pady=1)

# ROW 2 :

    btn2Pi = Button(calc, text="2pi", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.tau
				).grid(row=2, column=4, pady=1)

    btnCosh = Button(calc, text="Cosh", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.cosh
				).grid(row=2, column=5, pady=1)

    btntanh = Button(calc, text="tanh", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.tanh
				).grid(row=2, column=6, pady=1)

    btnsinh = Button(calc, text="sinh", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.sinh
				).grid(row=2, column=7, pady=1)

# ROW 3 :

    btnlog = Button(calc, text="log", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.log
				).grid(row=3, column=4, pady=1)

    btnExp = Button(calc, text="exp", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.exp
				).grid(row=3, column=5, pady=1)

    btnMod = Button(calc, text="Mod", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=lambda: added_value.operation("mod")
				).grid(row=3, column=6, pady=1)

    btnE = Button(calc, text="e", width=6,
			height=2, bg='black', fg='white',
			font=('Helvetica', 20, 'bold'),
			bd=4, command=added_value.e
			).grid(row=3, column=7, pady=1)

# ROW 4 :

    btnlog10 = Button(calc, text="log10", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.log10
				).grid(row=4, column=4, pady=1)

    btncos = Button(calc, text="log1p", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.log1p
				).grid(row=4, column=5, pady=1)

    btnexpm1 = Button(calc, text="expm1", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.expm1
				).grid(row=4, column=6, pady=1)

    btngamma = Button(calc, text="gamma", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.lgamma
				).grid(row=4, column=7, pady=1)
# ROW 5 :

    btnlog2 = Button(calc, text="log2", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.log2
				).grid(row=5, column=4, pady=1)

    btndeg = Button(calc, text="deg", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.degrees
				).grid(row=5, column=5, pady=1)

    btnacosh = Button(calc, text="acosh", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.acosh
				).grid(row=5, column=6, pady=1)

    btnasinh = Button(calc, text="asinh", width=6,
				height=2, bg='black', fg='white',
				font=('Helvetica', 20, 'bold'),
				bd=4, command=added_value.asinh
				).grid(row=5, column=7, pady=1)

    lblDisplay = Label(calc, text="Scientific Calculator",
				font=('Helvetica', 30, 'bold'),
				bg='black', fg='white', justify=CENTER)
    lblDisplay.grid(row=0, column=4, columnspan=4)
