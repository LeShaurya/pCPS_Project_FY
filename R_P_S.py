from tkinter import *
from random import randint
from tkinter import ttk

def spin():
    pick = randint(0,2)
    label_1.config(image = Image_list[pick],bd=0)
    
    if user_choice.get()=='Rock':
        user_choice_value = 0
    elif user_choice.get()=='Paper':
        user_choice_value = 1
    elif user_choice.get()=='Scissor':
        user_choice_value = 2
        
    
    if user_choice_value == 0:
        if pick == 0:
            Won_Lost.config(text = "It's a Tie ! Spin Again...")
        elif pick == 1:
            Won_Lost.config(text = "Paper Covers Rock! You Lose...")
        elif pick == 2:
            Won_Lost.config(text = "Rock Beats Scissor! You Win...")
    elif user_choice_value == 1:
        if pick == 1:
            Won_Lost.config(text = "It's a Tie ! Spin Again...")
        elif pick == 0:
            Won_Lost.config(text = "Paper covers Rock! You Win...")
        elif pick == 2:
            Won_Lost.config(text = "Scissor Cuts Paper! You Lose...")
    elif user_choice_value == 2:
        if pick == 2:
            Won_Lost.config(text = "It's a Tie ! Spin Agian...")
        elif pick == 1:
            Won_Lost.config(text = "Scissors Cuts Paper! You Win...")
        elif pick == 0:
            Won_Lost.config(text = "Rock Beats Scissor! You Lose...") 
            
            


window = Tk()
window.title('(: Rock-Paper-Scissors :)')
window.geometry('800x800')

window.config(bg='white')

Rock = PhotoImage(file = 'Rock.png')
Paper = PhotoImage(file = 'Paper.png')
Scissor = PhotoImage(file = 'Scissors.png')

Image_list = [Rock,Paper,Scissor]

pick = randint(0,2)

label_1 = Label(window, image = Image_list[pick],bd=0)
label_1.pack(pady=20)

btn_1 = Button(window,text = 'Spin!',command = spin)
btn_1.pack(pady=15)

user_choice = ttk.Combobox(window, value = ('Rock','Paper','Scissor'))
user_choice.current(0)
user_choice.pack(pady=25)

Won_Lost = Label(window,text='',font=('Aerial',18),bg='violet',fg='pink')
Won_Lost.pack(pady=40)


window.mainloop()
