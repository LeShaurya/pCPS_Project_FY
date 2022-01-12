#By Shauryadeep

import tkinter
from tkinter import messagebox
from tkinter import *
import random
from string import ascii_uppercase


window = tkinter.Tk()
window.title("Hangman")
p1 = PhotoImage(file = 'hang11.png')

window.iconphoto(False, p1)

window.resizable(0, 0)
window.configure(bg='#06d6a0')


my_file = open('commonword.txt')
all_the_lines = my_file.readlines()
items = []
for i in all_the_lines:
    items.append(i.upper())

word_list = [x[:-1] for x in items]


photos = [PhotoImage(file="hang0.png"),PhotoImage(file="hang1.png"),PhotoImage(file="hang2.png"),PhotoImage(file="hang3.png"),
          PhotoImage(file="hang4.png"),PhotoImage(file="hang5.png"),PhotoImage(file="hang6.png"),PhotoImage(file="hang7.png"),
          PhotoImage(file="hang8.png"),PhotoImage(file="hang9.png"),PhotoImage(file="hang10.png"),PhotoImage(file="hang11.png")]

def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    global the_word
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_list)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))

def guess(letter):
  global numberOfGuesses
  if numberOfGuesses<11:
    txt=list(the_word_withSpaces)
    guessed=list(lblWord.get())
    if the_word_withSpaces.count(letter)>0:
      for c in range(len(txt)):
        if txt[c]==letter:
          guessed[c]=letter
        lblWord.set("".join(guessed))
        if lblWord.get()==the_word_withSpaces:
          messagebox.showinfo("Hangman",f"You guessed it!")
          newGame() 
          
    else:
        numberOfGuesses+=1
        imgLabel.config(image=photos[numberOfGuesses])
        if numberOfGuesses==11:
          messagebox.showwarning("Hangman",f"Game over  \nThe Word is {the_word}")      

imgLabel = Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady= 40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24"),bg='#ffd166').grid(row=0, column=3, columnspan=6, padx=10)

n = 0 
for c in ascii_uppercase:
  Button(window, text=c, command= lambda c=c: guess(c), font= ("Helvetica 18"),bg='#118ab2',fg='#073b4c',width=5).grid(row=1+n//9, column=n%9)
  n+=1

Button(window, text="New\nGame", command=lambda:newGame(), font=("Helvetica 10 bold"),bg='#ef476f',fg='white').grid(row=3, column=8, sticky="NSWE")

newGame()
window.mainloop()




