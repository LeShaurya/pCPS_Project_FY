from tkinter import Tk
from tkinter.ttk import Button
import tkinter
from tkinter import messagebox
from tkinter import *
import os

root = Tk()
root.title("GAMES")
p1 = PhotoImage(file = 'game logo.png')
root.iconphoto(False, p1)
root.geometry("400x300")
root.resizable(0, 0)
root.configure(bg='#4cc9f0')

def open_file1():    
    os.startfile("Hangmancopy.py")
def open_file2():    
    os.startfile("NoughtsCrosses.py")
def open_file3():    
    os.startfile("R_P_S.py")

open_b = Button(root, text="PLAY HangMan",font= ("Helvetica 16 bold"),bg='#560bad',fg='#f8f9fa',bd=0,command=open_file1)    
open_b.pack(padx=20,pady=20)
open_a = Button(root, text="PLAY NoughtsCrosses",font= ("Helvetica 16 bold"),bg='#b5179e',fg='#f8f9fa',bd=0, command=open_file2)    
open_a.pack(padx=20,pady=20)
open_c = Button(root, text="PLAY Rock Paper Scissors",font= ("Helvetica 16 bold"),bg='#f72585',fg='#f8f9fa',bd=0,command=open_file3)    
open_c.pack(padx=20,pady=20)

root.mainloop()
