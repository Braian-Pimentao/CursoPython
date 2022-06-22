from tkinter import *

canvas = Canvas(width=400, height=300, bg='white')
canvas.pack(expand=NO, fill=NONE)
canvas.create_line(0, 0, 400, 300, fill='red')

canvas = Canvas()

mainloop()
