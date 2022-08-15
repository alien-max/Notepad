# https://alien-max.github.io/
from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root = Tk()
root.title("Notepad")
root.geometry("644x600+350+40")
textarea = scrolledtext.ScrolledText(root, font = "lucida 13")
textarea.pack(expand=True, fill=BOTH)

file = None

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)

def newfile():
    global file
    root.title("Untitled - Notepad")
    textarea.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt")
    filetypes = [("Text Documents", "*.txt")]
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+ " - Notepad")
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(defaultextension=".txt")
        filetypes = [("All Files","*.txt"), ("Text Documents", "*.txt")]

        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+ " - Notepad")
    
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()

def exitfile():
    root.destroy()

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

filemenu.add_command(label="New", command = newfile)
filemenu.add_command(label="Open", command = openfile)
filemenu.add_command(label="Save", command = savefile)

filemenu.add_separator()
filemenu.add_command(label="Exit", command = exitfile)

editmenu.add_command(label="Cut", command = cut)
editmenu.add_command(label="Copy", command = copy)
editmenu.add_command(label="Paste", command = paste)

root.mainloop()