from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
# Fuctional Part of this method

def clear():
    emailEntry.delete(0,END)
    UserEntry.delete(0,END)
    PasswordEntry.delete(0,END)
    ConfirmEntry.delete(0,END)
    check.set(0)

def connectDB():
    if emailEntry.get()==''or UserEntry.get()==''or PasswordEntry.get()==''or ConfirmEntry.get()=='':
        messagebox.showerror('Error','All Fields be Required')

    elif PasswordEntry.get() != ConfirmEntry.get():
        messagebox.showerror('Error','Password not Match')

    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms & Conditoion.')

    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='Ajinath@8545')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again0')
            return

        try:
            query = 'CREATE DATABASE jobhiring'
            mycursor.execute(query)
            query ='USE jobhiring'
            mycursor.execute(query)
            query = 'CREATE TABLE signup(id int auto_increment PRIMARY KEY not null, email varchar(30), username varchar(30), Password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('USE Jobhiring')   

        query = 'select * from signup where username=%s'
        mycursor.execute(query,(UserEntry.get()))

        row = mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Username Already Exists')

        else:
            query = 'INSERT INTO signup(email,username,Password ) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),UserEntry.get(),PasswordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is Successful.') 
            clear()
            signup_window.destroy()
            import SignIn

def loginpage():
    signup_window.destroy()
    import SignIn

# GUI Part 
signup_window = Tk()

signup_window.geometry('990x640+100+10')
signup_window.title('Sign Up Page')
signup_window.resizable(False,False)

bgIm = ImageTk.PhotoImage(file='bg.jpg')
bglabel = Label(signup_window,image=bgIm) 
bglabel.grid()

frame = Frame(signup_window,width=50,height=50,bg='white')
frame.place(x=300,y=100)

heading = Label(frame ,text='CREATE AN ACCOUNT',font=('arial',26,'italic'),
                fg='black',bg='white')
heading.grid(row=0,column=0,pady=10,padx=10)

email = Label(frame,text='Email',font=('Microsoft Yahei UI light',12,'bold'),bg='white')
email.grid(row=1,column=0,sticky='w',pady=(10,0),padx=80)
emailEntry = Entry(frame,font=('Microsoft Yahei UI light',12,'bold'),bg='white',width=24)
emailEntry.grid(row=2,column=0,sticky='w',padx=80)

User = Label(frame,text='Username',font=('Microsoft Yahei UI light',12,'bold'),bg='white')
User.grid(row=3,column=0,sticky='w',pady=(10,0),padx=80)
UserEntry = Entry(frame,font=('Microsoft Yahei UI light',12,'bold'),bg='white',width=24)
UserEntry.grid(row=4,column=0,sticky='w',padx=80)

Password = Label(frame,text='Password',font=('Microsoft Yahei UI light',12,'bold'),bg='white')
Password.grid(row=5,column=0,sticky='w',pady=(10,0),padx=80)
PasswordEntry = Entry(frame,font=('Microsoft Yahei UI light',12,'bold'),bg='white',width=24)
PasswordEntry.grid(row=6,column=0,sticky='w',padx=80)

Confirm = Label(frame,text='Confirm',font=('Microsoft Yahei UI light',12,'bold'),bg='white')
Confirm.grid(row=7,column=0,sticky='w',pady=(15,0),padx=80)
ConfirmEntry = Entry(frame,font=('Microsoft Yahei UI light',12,'bold'),bg='white',width=24)
ConfirmEntry.grid(row=8,column=0,sticky='w',padx=80)

check = IntVar()
termandcon = Checkbutton(frame,text='I agree to the terms & conditions',font=('Microsoft Yahei UI light',10,'bold')
                         ,bg='white',activeforeground='black',activebackground='white',cursor='hand2',variable=check)
termandcon.grid(row=9,sticky='w',padx=80,pady=10)

signupbtn = Button(frame,text='SIGN UP',font=('Open sans',14,'bold'),bg='skyblue',width=17,bd=2,
                activeforeground='black',fg='black',activebackground='skyblue',cursor='hand2',command=connectDB)
signupbtn.grid(row=10,column=0,pady=10)

already = Label(frame,text="Don't have an account?",font=('Open sans',10,'bold'),bg='white')
already.grid(row=11,sticky='w',padx=70,pady=10)

loginbtn = Button(frame,text='Log In',font=('Open sans',10,'bold underline'),bd=0,
                  bg='white',cursor='hand2',activebackground='white',command=loginpage)
loginbtn.place(x=287,y=437)
signup_window.mainloop()