from tkinter import *

from tkinter import ttk
#
# 
#
#

def works(numberPressed):
    stringy = str(numberPressed)
    print("button was just pushed" + stringy)
    inty = int(stringy)
root = Tk()

root.title("calc bitch")
mainFrame = ttk.Frame(root,paddin="3 3 12 12")
mainFrame.grid(column=0,row=0, sticky=(N,W,E,S))
button1 = ttk.Button(mainFrame, text=1, command=works).grid(column=1, row=2, sticky=W) 
button2 = ttk.Button(mainFrame, text=2, command=works).grid(column=2, row=2, sticky=W) 
button3 = ttk.Button(mainFrame, text=3, command=works).grid(column=3, row=2, sticky=W)
button4 = ttk.Button(mainFrame, text=4, command=works).grid(column=1, row=3, sticky=W)
button5 = ttk.Button(mainFrame, text=5, command=works).grid(column=2, row=3, sticky=W)
button6 = ttk.Button(mainFrame, text=6, command=works).grid(column=3,row=3,sticky=W)
button7 = ttk.Button(mainFrame, text=7, command=works).grid(column=1,row=4, sticky=W)
button8 = ttk.Button(mainFrame, text=88, command=works).grid(column=2, row=4, sticky=W)
button9 = ttk.Button(mainFrame, text=9, command=works(9)).grid(column=3,row=4,sticky=W)
button0 = ttk.Button(mainFrame, text=0, command=works).grid(column=1, row=5, sticky=W)
buttonDel = ttk.Button(mainFrame, text="Del", command=works).grid(column=2, row=5, sticky=W)


root.mainloop()

