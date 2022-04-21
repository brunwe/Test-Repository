import tkinter as tk

root = tk.Tk()
root.title("Celsius to Fahrenheit Calculator")
root.geometry('400x200+50+50')
root.resizable(False, False)

output = 0
greeting = tk.Label(text="Coded by Will Brunner")

entry1 = tk.Entry()
entry1.place(x=25, y=85)

label1 = tk.Label(text=int(output), width=15)
label1.place(x=300, y=85)


def calculate():
    label1["text"] = 9 / 5 * int(entry1.get()) + 32


button1 = tk.Button(text="convert to F", command=calculate)
button1.place(x=165, y=80)

greeting.pack()

root.mainloop()
