from tkinter import *
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    textarea.delete(1.0, END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents","*.txt")])
    # no file to open
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+ " - Notepad")
        textarea.delete(1.0, END)
        f=open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        #save as new file
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),

                                            ("Text Documents", "*.txt")])

        # no file to open
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

        root.title(os.path.basename(file) + " - Notepad")
        #print("File Saved")
    else:
        # Save the already openend and saved before file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()
        #print("hu")


def cut():
    textarea.event_generate("<<Cut>>")
def copy():
    textarea.event_generate("<<Copy>>")
def paste():
    textarea.event_generate("<<Paste>>")
def about():
    tmsg.showinfo("Notepad","Notepad by Shagun")

if __name__ == '__main__':

    #basic setup
    root = Tk()
    root.geometry("500x500")
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad (1).ico")



    # text area
    textarea=Text(root, font="lucida 19")
    textarea.pack(fill=BOTH, expand=TRUE)
    #expand bolta h true hone pr parent ki puri width le elga text area

    file= None
    #point to the current file open

    # scrollbar
    s1 = Scrollbar(textarea)
    s1.pack(side=RIGHT, fill=Y)
    s1.config(command=textarea.yview)
    textarea.config(yscrollcommand=s1.set)

    #menubar
    Menubar=Menu(root)


    #file menu starts
    Filemenu=Menu(Menubar, tearoff=0)
    #to open new file
    Filemenu.add_command(label="New", command=newFile)
    #to open already existing file
    Filemenu.add_command(label="Open", command=openFile)
    #to save a file
    Filemenu.add_command(label="Save", command=saveFile)
    Filemenu.add_separator()
    #to exit
    Filemenu.add_command(label="Exit", command=exit)

    Menubar.add_cascade(label="File", menu=Filemenu)
    #file menu ends


    #edit menu starts
    EditMenu=Menu(Menubar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    Menubar.add_cascade(label="Edit", menu=EditMenu)
    #edit menu ends


    #help starts
    HelpMenu=Menu(Menubar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    Menubar.add_cascade(label="Help", menu=HelpMenu)
    #help ends

    root.config(menu=Menubar)



    root.mainloop()