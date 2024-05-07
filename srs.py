from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox
import pymysql

#Funkcijos
count = 0
text = ''
def slider():
    global text, count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    headerLabel.config(text=text)
    count+=1
    headerLabel.after(300,slider)

def clock():
    date=time.strftime('%d/%m/%Y')
    currtime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f' Data:{date} \nLaikas:{currtime}')
    datetimeLabel.after(1000,clock)

def add_student():
    add_window=Toplevel()
    idLabel=Label(add_window)

def connect_database():
    def connect():
        try:
            con=pymysql.connect(host='localhost',user='root',password='admin')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Klaida','Neteisingi duomenys',parent=connectWindow)
            return
        
        query='use studentdata'
        mycursor.execute(query)
        messagebox.showinfo('Success','Prisijungete prie duomenu bazes',parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Prisijungimas prie duomenu bazes')
    connectWindow.resizable(False,False)

    hostnameLabel=ttk.Label(connectWindow,text='Host Name',font=('Roboto',16,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)
    hostEntry=Entry(connectWindow,bd=2,font=('roboto',16))
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel=ttk.Label(connectWindow,text='User Name',font=('Roboto',16,'bold'))
    usernameLabel.grid(row=1,column=0,padx=20)
    usernameEntry=Entry(connectWindow,bd=2,font=('roboto',16))
    usernameEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordLabel=ttk.Label(connectWindow,text='Password',font=('Roboto',16,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)
    passwordEntry=Entry(connectWindow,bd=2,font=('roboto',16))
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)

    connectButton=ttk.Button(connectWindow,text='Prisijungti',command=connect)
    connectButton.grid(row=3,column=1)

#GUI
root=ttkthemes.ThemedTk()

root.geometry('1174x688+0+0')
root.title('Studentu registracijos sistema')
root.resizable(False,False)
root.get_themes()
root.set_theme('radiance')

datetimeLabel=Label(root,text='hello',font=('Roboto',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()


s='Studentu Registracijos Sistema'
headerLabel=Label(root,text=s,font=('Roboto',28,'italic bold'), width=30)
headerLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='Prisijungti prie duomenu bazes',command=connect_database)
connectButton.place(x=870,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='students.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

#LEFT FRAME MYGTUKAI
addstudentButton=ttk.Button(leftFrame, text='Prideti Studenta',width=25, state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame, text='Ieskoti Studento',width=25, state=DISABLED)
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame, text='Salinti Studenta',width=25, state=DISABLED)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame, text='Atnaujinti Studenta',width=25, state=DISABLED)
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame, text='Rodyti Studenta',width=25, state=DISABLED)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame, text='Eksportuoti duomenis',width=25, state=DISABLED)
exportstudentButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame, text='Iseiti',width=25)
exitButton.grid(row=7,column=0,pady=20)

#RIGHT FRAME

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollbarX=ttk.Scrollbar(rightFrame,orient=HORIZONTAL)
scrollbarY=ttk.Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('ID','Vardas','Mob.Numeris','El.pastas','Lytis','Gim.Metai','Prideta data','Pridetas laikas'),xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)

scrollbarX.config(command=studentTable.xview)
scrollbarY.config(command=studentTable.yview)

scrollbarX.pack(side=BOTTOM,fill=X)
scrollbarY.pack(side=RIGHT,fill=Y)
studentTable.pack(fill=BOTH,expand=1)


studentTable.heading('ID',text='ID')
studentTable.heading('Vardas',text='Vardas')
studentTable.heading('Mob.Numeris',text='Mob.Numeris')
studentTable.heading('El.pastas',text='Elektroninis Pastas')
studentTable.heading('Lytis', text='Lytis')
studentTable.heading('Gim.Metai', text='Gim.Metai')
studentTable.heading('Prideta data', text='Prideta data')
studentTable.heading('Pridetas laikas', text='Pridetas laikas')
studentTable.config(show='headings')



root.mainloop()
