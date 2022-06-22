#import modules......................
from itertools import count
from tkinter import *
from tkinter import messagebox     
from random import randint,choice,shuffle
import pyperclip                   
import string


#Initializing lists of characters............
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#letters=string.ascii_letters
#letters=list(letters)

#Function to generating the password ...............................
def password_generator():
    password_list = []
    for char in range(randint(8, 10)):
      password_list.append(choice(letters))

    for char in range(randint(2, 4)):
      password_list += choice(symbols)

    for char in range(randint(2, 4)):
      password_list += choice(numbers)

    shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    input_password.insert(0,password)
    print(f"Your password is: {password}")

#function for saving the password in txt file........................
#i=1
#while(i<10):
def save_data():
    name_website = input_website.get()
    name_email = input_email.get()
    name_password = input_password.get()

    with open('password.txt','w') as data:
        if len(name_website)==0 or len(name_email)==0 or len(name_password)==0:
            show_msg = messagebox.showinfo(title="Fill", message="Missed a feild\n If not required,fill NA")
        else:
            show_msg = messagebox.askokcancel(title="Confirm?",
                                            message=f"Website: {name_website}\nUsername: {name_email}\nPassword: {name_password}\nSave?")
            if show_msg:
              #counter=1
              #while(counter<10):
                
                data.write(f"{name_website} ---------- {name_email} ---------- {name_password}\n")
                show_msg = messagebox.showinfo(title="Saving...", message="Successfully Saved")
                input_password.delete(0, END)
                input_website.delete(0, END)
                input_email.delete(0,END)
                

               # counter+=1
#to copy password    
def copy_pass():
  password = input_password.get()
  pyperclip.copy(password)
  show_msg=messagebox.showinfo(title="Copy",message="Password copied to clipboard\n***************")

#GUI
#Window setup
window=Tk()
window.title("PASSWORD GENERATOR")
window.config(bg='white',padx=500, pady=250,background='#FFC395')

#adding image
canvas = Canvas(width=200, height=200,bg="white",highlightthickness=0)
logo_img=PhotoImage(file="images.png")
canvas.create_image(100,100,image=logo_img)     #adding logo
canvas.grid(row=0,column=1)

#webisite label:
website_label= Label(text="Website:")
website_label.grid(row=1,column=0)
input_website=Entry(width=50)
input_website.grid(row=1,column=1,columnspan=2)
input_website.focus()   #Puts cursor in textbox.

#username label
email_label= Label(text="Username:")
email_label.grid(row=2,column=0)
input_email=Entry(width=50,)
input_email.grid(row=2,column=1,columnspan=2)

#password label
password_label= Label(text="Password:")
password_label.grid(row=3,column=0)
input_password=Entry(width=25)
input_password.grid(row=3,column=1)

#Button for password generator
password_button=Button(text='Generate Password',command=password_generator,activebackground='red')#password generator as command for password generator button
password_button.grid(row=3,column=2)

#Button for adding data into txt file
add_button=Button(text='Save',width=66,command=save_data,activebackground='red')#save data as command for add button
add_button.grid(row=5,column=1,columnspan=2)

#Copy_button
clip_board_button=Button(text='Copy',width=36,command=copy_pass,activebackground='red')
clip_board_button.grid(row=4,column=1,columnspan=2)

#Run the GUI
window.mainloop()