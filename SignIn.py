from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
#  Fuctionality Part In this Method

def ForgetPas():
    def changePassword():
        if User_Entry.get()=='' or newEntry.get()=='' or ConfirmEntry.get()=='':
            messagebox.showerror('Error','All Fields are Required',parent=resetwindow)
        elif newEntry.get()!=ConfirmEntry.get():
            messagebox.showerror('Error','Password & Confirm Password not Match',parent=resetwindow)

        else:
            con = pymysql.connect(host='localhost',user='root',password='Ajinath@8545',database='jobhiring')
            mycursor = con.cursor()        
            query = 'SELECT * FROM signup where username=%s'
            mycursor.execute(query,(User_Entry.get()))
            row = mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username')
            else:
                query = 'update signup set password=%s where username=%s'
                mycursor.execute(query,(newEntry.get(),User_Entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, Please Login with new password')
                resetwindow.destroy()   

    resetwindow = Toplevel()

    resetwindow.geometry('990x640+100+10')
    resetwindow.title('Change Password')
    resetwindow.resizable(False,False)
 
    bgIm = ImageTk.PhotoImage(file='bg.jpg')
    bglabel = Label(resetwindow,image=bgIm)
    bglabel.place(x=0,y=0)

    frame = Frame(resetwindow,width=40,height=50,bg='white')
    frame.place(x=300,y=100)

    heading = Label(frame ,text='RESET PASSWORD',font=('arial',26,'italic'),
                fg='blue',bg='white')
    heading.grid(row=0,column=0)

    User = Label(frame,text='Username',font=('Microsoft Yahei UI light',12,'bold'),bg='white',fg='blue')
    User.grid(row=1,column=0,sticky='w',pady=(20,0),padx=80)
    User_Entry = Entry(frame,font=('Microsoft Yahei UI light',12,'bold'),bg='white',fg='blue',width=24,bd=0)
    User_Entry.grid(row=2,column=0,sticky='w',padx=80,pady=(0,10))

    frame1 = Frame(frame,width=245,height=2,bg='blue')
    frame1.grid(row=2,column=0,padx=80,pady=(25,10),sticky='w')

    Password = Label(frame,text='New Password',font=('Microsoft Yahei UI light',12,'bold'),bg='white',fg='blue')
    Password.grid(row=3,column=0,sticky='w',pady=(20,0),padx=80)
    newEntry = Entry(frame,font=('Microsoft Yahei UI light',12,'bold'),bg='white',fg='blue',width=24,bd=0)
    newEntry.grid(row=4,column=0,sticky='w',padx=80,pady=(0,10))

    frame2 = Frame(frame,width=245,height=2,bg='blue')
    frame2.grid(row=4,column=0,padx=80,pady=(25,10),sticky='w')

    Confirm = Label(frame,text='Confirm Password',font=('Microsoft Yahei UI light',12,'bold'),bg='white',fg='blue')
    Confirm.grid(row=5,column=0,sticky='w',pady=(20,0),padx=80)
    ConfirmEntry = Entry(frame,font=('Microsoft Yahei UI light',12,'bold'),bg='white',fg='blue',width=24,bd=0)
    ConfirmEntry.grid(row=6,column=0,sticky='w',padx=80,pady=(0,10))

    frame2 = Frame(frame,width=245,height=2,bg='blue')
    frame2.grid(row=6,column=0,padx=80,pady=(25,10),sticky='w')

    submitbtn = Button(frame,text='SUBMIT',font=('open sans',14,'bold'),width=15,bg='red',
                     fg='white',cursor='hand2',bd=3,activeforeground='white',activebackground='red',command=changePassword)
    submitbtn.grid(row=7,column=0,pady=(30,50),padx=10)

    resetwindow.mainloop()

def loginuser():
    if userEntry.get()==''or PassEntry.get()=='':
        messagebox.showerror('Error','All Fields are Required')

    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='Ajinath@8545')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Connection not Established try Again')
            return
        
        query = 'USE jobhiring'
        mycursor.execute(query)
        query = 'SELECT * FROM signup where username=%s and password=%s'
        mycursor.execute(query,(userEntry.get(),PassEntry.get()))
        row = mycursor.fetchone()
        if row ==None:
            messagebox.showerror('Error','Invalid Username & Password')
        else:
            messagebox.showinfo('Welcome','Login Successful')
            Login_Window.destroy()
            import SignIn
              
def SignUpPage():
    Login_Window.destroy()
    import SignUp

def hide():
    viewEye.config(file='hidden.png')
    PassEntry.config(show='*')
    eyebtn.config(command=show)

def show():
    viewEye.config(file='view.png')
    PassEntry.config(show='')
    eyebtn.config(command=hide)

def userEnter(event):
    if userEntry.get()=='Username':
        userEntry.delete(0,END)

def passEnter(event):
    if PassEntry.get()=='Password':
        PassEntry.delete(0,END)

#  GUI Part In Desktop
Login_Window  = Tk()

Login_Window .geometry('990x640+100+10')
Login_Window .title('Login Page')
Login_Window .resizable(False,False)
 
bgIm = ImageTk.PhotoImage(file='bg.jpg')
bglabel = Label(Login_Window,image=bgIm)
bglabel.place(x=0,y=0)

frame = Frame(Login_Window,width=40,height=50,bg='white')
frame.place(x=300,y=100)

heading = Label(frame ,text='USER LOGIN',font=('arial',26,'italic'),
                fg='blue',bg='white')
heading.grid(row=0,column=0)

userEntry = Entry(frame ,width=25,font=('Microsoft Yahei UI light',12,'bold '),
                  bd=0,fg='blue',bg='white')
userEntry.grid(row=1,column=0,padx=50,sticky='e',pady=(40,10))
userEntry.insert(0,'Username')
userEntry.bind('<FocusIn>',userEnter)
frame1 = Frame(frame,width=200,height=2,bg='blue')
frame1.grid(row=1,column=0,padx=50,pady=(59,10),sticky='w')

PassEntry = Entry(frame ,width=25,font=('Microsoft Yahei UI light',12,'bold'),
                  bd=0,fg='blue',bg='white')
PassEntry.grid(row=2,column=0,sticky='e',padx=50,pady=10)
PassEntry.insert(0,'Password')
PassEntry.bind('<FocusIn>',passEnter)
frame2 = Frame(frame,width=200,height=2,bg='blue')
frame2.grid(row=2,column=0,padx=50,pady=(29,10),sticky='w')

viewEye = PhotoImage(file='view.png')
eyebtn = Button(frame,image=viewEye,bd=0,cursor='hand2',command=hide,bg='white',activebackground='white')
eyebtn.grid(row=2,column=0,pady=(10,10),padx=100,sticky='e')

forgetbtn = Button(frame,text='Forgot Password?',bg='white',font=('Microsoft Yahei UI light',9,'bold'),
                   width=15,bd=0,fg='blue',cursor='hand2',activeforeground='blue',activebackground='white',command=ForgetPas)
forgetbtn.grid(row=3,column=0,sticky='e',padx=90,pady=10)

loginbtn = Button(frame,text='LOGIN',font=('open sans',14,'bold'),width=21,bg='red',
                 fg='white',cursor='hand2',bd=3,activeforeground='white',activebackground='red',command=loginuser)
loginbtn.grid(row=4,column=0,pady=10,padx=10)

orlabel = Label(frame,text='------------------- OR -------------------',bg='white',font=('open sans',14),fg='blue')
orlabel.grid(row=5,column=0,pady=10,padx=10)

fblogo = PhotoImage(file='facebook.png')
fblabel = Label(frame,image=fblogo,bg='white')
fblabel.place(x=80,y=340)

googlelogo = PhotoImage(file='search.png')
googlelabel = Label(frame,image=googlelogo,bg='white')
googlelabel.place(x=160,y=340)

twitterlogo = PhotoImage(file='twitter.png')
twitterlabel = Label(frame,image=twitterlogo,bg='white')
twitterlabel.place(x=240,y=340)

signuplabel = Label(frame,text="Don't have an account.",font=('open sans',10),fg='blue',bg='white')
signuplabel.grid(row=8,columnspan=1,pady=(100,10),sticky='w',padx=40)
newaccounbtn = Button(frame,text='Create new account',font=('open sans',10,'bold underline'),bg='white',width=18,
                 fg='blue',cursor='hand2',activebackground='white',bd=0,activeforeground='blue',command=SignUpPage )
newaccounbtn.grid(row=8,columnspan=2,pady=(100,10),sticky='e',padx=20)

frame .mainloop()