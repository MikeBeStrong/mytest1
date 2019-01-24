#-*- coding:utf8 -*-
#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into 
# a single PDF.

import PyPDF2, os,time

import tkinter as tk
from tkinter import filedialog
 
window = tk.Tk()

count = 0


def buttonClick():
    global count
    count = count + 1
    button.config(text=str(count))


button=tk.Button(window,text='点我', command=buttonClick)
button.pack()
window.mainloop()

