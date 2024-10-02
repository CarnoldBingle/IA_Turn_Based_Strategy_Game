

import tkinter as tk


root = tk.Tk()

root.title()
root.geometry("1000x600")
root.resizable(False, False)
root.config(bg="green")

canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
canvas.place(x=450, y=50)
oval = canvas.create_oval(10, 10, 90, 40, fill="red", outline="black")
canvas.create_text(50, 25, text="ST", font=("Arial", 12, "bold"))

canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
canvas.place(x=275, y=100)
oval = canvas.create_oval(10, 10, 90, 40, fill="red", outline="black")
canvas.create_text(50, 25, text="LW", font=("Arial", 12, "bold"))

canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
canvas.place(x=625, y=100)
oval = canvas.create_oval(10, 10, 90, 40, fill="red", outline="black")
canvas.create_text(50, 25, text="RW", font=("Arial", 12, "bold"))

canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
canvas.place(x=450, y=525)
oval = canvas.create_oval(10, 10, 90, 40, fill="yellow", outline="black")
canvas.create_text(50, 25, text="GK", font=("Arial", 12, "bold"))

canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
canvas.place(x=550, y=425)
oval = canvas.create_oval(10, 10, 90, 40, fill="Blue", outline="black")
canvas.create_text(50, 25, text="CB", font=("Arial", 12, "bold"))

canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
canvas.place(x=350, y=425)
oval = canvas.create_oval(10, 10, 90, 40, fill="Blue", outline="black")
canvas.create_text(50, 25, text="CB", font=("Arial", 12, "bold"))

canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
canvas.place(x=250, y=375)
oval = canvas.create_oval(10, 10, 90, 40, fill="Blue", outline="black")
canvas.create_text(50, 25, text="LB", font=("Arial", 12, "bold"))

canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
canvas.place(x=650, y=375)
oval = canvas.create_oval(10, 10, 90, 40, fill="Blue", outline="black")
canvas.create_text(50, 25, text="RB", font=("Arial", 12, "bold"))

canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
canvas.place(x=350, y=225)
oval = canvas.create_oval(10, 10, 90, 40, fill="Purple", outline="black")
canvas.create_text(50, 25, text="CM", font=("Arial", 12, "bold"))

canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
canvas.place(x=550, y=225)
oval = canvas.create_oval(10, 10, 90, 40, fill="Purple", outline="black")
canvas.create_text(50, 25, text="CM", font=("Arial", 12, "bold"))

canvas = tk.Canvas(root, width=100, height=50, bg="green", highlightthickness=0)
canvas.place(x=450, y=300)
oval = canvas.create_oval(10, 10, 90, 40, fill="Purple", outline="black")
canvas.create_text(50, 25, text="CDM", font=("Arial", 12, "bold"))

root.mainloop()
