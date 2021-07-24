# sneaky sneak 3
# v1.0

from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from ciphers import *

filepath = ''

def new_file():
    global filepath
    filepath = ''
    textedit.delete(1.0, END)
    root.title('Sneaky Sneak 3 - New File')

def open_file():
    global filepath
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    if not filepath:
        return
    textedit.delete(1.0, END)
    
    with open(filepath, "r") as input_file:
        text = input_file.read()
        textedit.insert(END, text)
    root.title(f"Sneaky Sneak 3 - {filepath}")
    
def save_file():
    global filepath
    if filepath == '':
        save_as_file()
    else:
        with open(filepath, "w") as output_file:
            text = textedit.get(1.0, END)
            output_file.write(text)
        root.title(f"Sneaky Sneak 3 - {filepath}")
    
def save_as_file():
    global filepath
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:
        text = textedit.get(1.0, END)
        output_file.write(text)
    root.title(f"Sneaky Sneak 3 - {filepath}")
    
def rot13_encode():
    text = textedit.get(1.0, END)
    textedit.delete(1.0, END)
    encoded = rot13(text)
    textedit.insert(END, encoded)

def atbash_encode():
    text = textedit.get(1.0, END)
    textedit.delete(1.0, END)
    encoded = atbash(text)
    textedit.insert(END, encoded)

def ceasar_encode():
    key = askinteger('Enter Key', 'Please enter key for ceasar cipher')
    text = textedit.get(1.0, END)
    textedit.delete(1.0, END)
    encoded = ceasar(key, text)
    textedit.insert(END, encoded)

def ceasar_decode():
    key = -(askinteger('Enter Key', 'Please enter key for ceasar cipher'))
    text = textedit.get(1.0, END)
    textedit.delete(1.0, END)
    decoded = ceasar(key, text)
    textedit.insert(END, decoded)
    
def vigenere_encode():
    key = askstring('Enter Key', 'Please enter key for vigenere cipher')
    text = textedit.get(1.0, END)
    textedit.delete(1.0, END)
    decoded = vigenere(key, text)
    textedit.insert(END, decoded)

def vigenere_decode():
    key = askstring('Enter Key', 'Please enter key for vigenere cipher')
    text = textedit.get(1.0, END)
    textedit.delete(1.0, END)
    decoded = beaufort(key, text)
    textedit.insert(END, decoded)

def idk():
    messagebox.showinfo('Sorry', 'This feature is still in development')

root = Tk()
root.title("Sneaky Sneak 3 - New File")

menubar =  Menu(root)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label='Save As', command = save_as_file)
menubar.add_cascade(label="File", menu=filemenu)

ciphermenu = Menu(menubar, tearoff = 0)

encodemenu = Menu(ciphermenu, tearoff = 0)
encodemenu.add_command(label='Atbash', command=atbash_encode)
encodemenu.add_command(label='ROT13', command=rot13_encode)
encodemenu.add_command(label='Ceasar', command=ceasar_encode)
encodemenu.add_command(label='Vigenere', command=vigenere_encode)
ciphermenu.add_cascade(label = 'Encode', menu = encodemenu)

decodemenu = Menu(ciphermenu, tearoff = 0)
decodemenu.add_command(label='Atbash', command=atbash_encode)
decodemenu.add_command(label='ROT13', command=rot13_encode)
decodemenu.add_command(label='Ceasar', command=ceasar_decode)
decodemenu.add_command(label='Vigenere', command=vigenere_decode)
decodemenu.add_separator()
decodemenu.add_command(label='Detect', command = idk)
ciphermenu.add_cascade(label='Decode', menu=decodemenu)

menubar.add_cascade(label = 'Cipher', menu = ciphermenu)

scrollbar = Scrollbar(root)
textedit = Text(root, wrap = WORD)
scrollbar.pack(side=RIGHT, fill=Y)
textedit.pack(side=LEFT, expand=True, fill=BOTH)
scrollbar.config(command=textedit.yview)
textedit.config(yscrollcommand=scrollbar.set)

root.config(menu=menubar)
root.mainloop()