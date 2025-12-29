from tkinter import *

root = Tk()

def run(funcid = None):
    for i in range(0,5):
        print("i did it")

button = Button(root, text="hi", command=run)
button.pack()


root.mainloop()