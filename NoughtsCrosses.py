from tkinter import *
from tkinter import messagebox
import tkinter.font as font

tk = Tk()
tk.title("Noughts & Crosses")

clicked = True
count = 0

label = Label( tk, text="Noughts & Crosses")
label.grid(row=0, column=1)

#Creating buttons/reset button.
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9, clicked, count
    b1=Button(tk, text=" ", height=6, width=12, command=lambda:bclick(b1))
    b2=Button(tk, text=" ", height=6, width=12, command=lambda:bclick(b2))
    b3=Button(tk, text=" ", height=6, width=12, command=lambda:bclick(b3))

    b4=Button(tk, text=" ", height=6, width=12, command=lambda:bclick(b4))
    b5=Button(tk, text=" ", height=6, width=12, command=lambda:bclick(b5))
    b6=Button(tk, text=" ", height=6, width=12, command=lambda:bclick(b6))

    b7=Button(tk, text=" ", height=6, width=12, command=lambda:bclick(b7))
    b8=Button(tk, text=" ", height=6, width=12, command=lambda:bclick(b8))
    b9=Button(tk, text=" ", height=6, width=12, command=lambda:bclick(b9))


    #Arranging our buttons.
    b1.grid(row=1, column=0)
    b2.grid(row=1, column=1)
    b3.grid(row=1, column=2)

    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)

    b7.grid(row=3, column=0)
    b8.grid(row=3, column=1)
    b9.grid(row=3, column=2)



#To tell if the button is clicked.
def bclick(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
       
        clicked = False
        wincheck()
        count += 1

    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
     
        clicked = True
        wincheck()
        count += 1

    else:
        messagebox.showerror("Wrong move!","This button is not empty.")


#To tell if anyone has won the game.
def wincheck():
    if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X'):
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 1 wins!")
    elif(b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X'):
        b4.config(fg="red")
        b5.config(fg="red")
        b6.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 1 wins!")
    elif(b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X'):
        b7.config(fg="red")
        b8.config(fg="red")
        b9.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 1 wins!")
    elif(b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X'):
        b1.config(fg="red")
        b5.config(fg="red")
        b9.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 1 wins!")
    elif(b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X'):
        b3.config(fg="red")
        b5.config(fg="red")
        b7.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 1 wins!")
    elif(b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X'):
        b1.config(fg="red")
        b4.config(fg="red")
        b7.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 1 wins!")
    elif(b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X'):
        b2.config(fg="red")
        b5.config(fg="red")
        b8.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 1 wins!")
    elif(b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
        b3.config(fg="red")
        b6.config(fg="red")
        b9.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 1 wins!")

    elif(count == 8):
        messagebox.showinfo("Noughts & Crosses", "It's a Tie.")

    elif(b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O'): 
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 2 wins!")

    elif(b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O'): 
        b4.config(fg="red")
        b5.config(fg="red")
        b6.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 2 wins!")

    elif(b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O'): 
        b7.config(fg="red")
        b8.config(fg="red")
        b9.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 2 wins!")

    elif(b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O'): 
        b1.config(fg="red")
        b5.config(fg="red")
        b9.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 2 wins!")

    elif(b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O'): 
        b3.config(fg="red")
        b5.config(fg="red")
        b7.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 2 wins!")

    elif(b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O'): 
        b1.config(fg="red")
        b4.config(fg="red")
        b7.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 2 wins!")

    elif(b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O'): 
        b2.config(fg="red")
        b5.config(fg="red")
        b8.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 2 wins!")

    elif(b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
        b3.config(fg="red")
        b6.config(fg="red")
        b9.config(fg="red")
        messagebox.showinfo("Noughts & Crosses", "Player 2 wins!")

#To reset.
reset1 = Button(text="Reset",command=reset)
reset1.grid(row=4, column=2)

reset()

tk.mainloop()
