import tkinter as tk
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("خطا")
            messagebox.showerror("خطا", "عبارت نادرست است")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("400x600")
root.title("ماشین حساب")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20 bold")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in button_texts:
    button_row = tk.Frame(buttons_frame)
    button_row.pack(expand=True, fill="both")
    for text in row:
        button = tk.Button(button_row, text=text, font="Arial 18", width=4, height=2)
        button.pack(side="left", expand=True, fill="both")
        button.bind("<Button-1>", click)

root.mainloop()
