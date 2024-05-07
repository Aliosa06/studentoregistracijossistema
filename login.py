import mysql.connector
from tkinter import*
from PIL import ImageTk
from tkinter import messagebox

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Klaida','Langai negali buti tusti')
    elif usernameEntry.get() == 'Alius' and passwordEntry.get() == '1234':
        messagebox.showinfo('Pavyko','Sveiki!')
        root.destroy()
        import srs    
    else:
        messagebox.showerror('Klaida','Iveskite teisingus duomenis')
    

################## LOGIN LANGAS #########################
root = Tk()
root.geometry('1280x720+0+0')
root.resizable(False,False)
root.title('Studento registravimo sistemos prisijungimas')


################## IMAGE IMPORTAI ########################
backgroundImage = ImageTk.PhotoImage(file='bg.png')
logoImage = ImageTk.PhotoImage(file='logoimage.png')
usernameImage = PhotoImage(file= 'user.png')
passwordImage = PhotoImage(file='password.png')

################## LOGIN FRAME GUI #######################

bgLabel=Label(root,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(root,bg='alice blue')
loginFrame.place(x=430,y=200)

logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,font=('Roboto',15,'bold'),bg='alice blue')
usernameLabel.grid(row=1,column=0,padx=20)
usernameEntry=Entry(loginFrame,font=('Roboto',15,'bold'),bd=3)
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT,font=('Roboto',15,'bold'),bg='alice blue')
passwordLabel.grid(row=2,column=0,padx=20)
passwordEntry=Entry(loginFrame,font=('Roboto',15,'bold'),bd=3)
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='Login',font=('Roboto',15,'bold'),width=15,fg="white",bg='cornflower blue',activebackground='cornflower blue',activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=5)








root.mainloop()







##GUI ELEMENTAI

