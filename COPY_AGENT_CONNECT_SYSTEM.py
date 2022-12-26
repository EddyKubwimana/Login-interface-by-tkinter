from tkinter import *
import bcrypt
import sqlite3
from tkinter import messagebox
import ast
mydb = sqlite3.connect("agent_connnect.db")
cursor = mydb.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user( username varchar(255), password varchar(255))")


# sign up from
class SignUp:
    
    def __init__(self, root):
        self.root = root
        self.Frame = Frame(Frame, width=350, height=390, bg="#fff")
        self.Frame.place(x=480, y=50)
        self.sign_uplabel = Label(Frame, text="SignUp", fg="#57a1f8", bg="White", font=("Microsoft Yahei UI Light", 23, "bold"))
        self.sign_uplabel.place(x=100, y=5)

        self.username = Entry(Frame, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
        self.username.place(x=80, y=80)
        self.Frame(Frame, width=295, height=2, bg="black").place(x=80, y=107)
        self.username.insert(0, "Username")
        self.username.bind("<FocusIn>", on_enter)
        self.username.bind("<FocusOut>", on_leave)

        self.password = Entry(Frame, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
        self.password.place(x=80, y=140)
        Frame(Frame, width=295, height=2, bg="black").place(x=80, y=167)
        self.insert(0, "Password")
        self.password.bind("<FocusIn>", p_enter)
        self.password.bind("<FocusOut>", p_leave)


        self.confirm_password = Entry(Frame, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
        self.confirm_password.place(x=80, y=200)
        self.Frame(Frame, width=295, height=2, bg="black").place(x=80, y=227)
        self.confirm_password.insert(0, "Confirm password")
        self.confirm_password.bind("<FocusIn>", cp_enter)
        self.confirm_password.bind("<FocusOut>", cp_leave)

    def on_enter(self,e):
            self.username.delete(0, "end")

    def on_leave(self,e):
            if self.username.get() == "":
                self.username.insert(0, "Username")

        # user confirm password

    def cp_enter(self,e):
            self.confirm_password.delete(0, "end")

    def cp_leave(self,e):
            if self.confirm_password.get() == "":
                self.confirm_password.insert(0, "Confirm password")
                

    def p_leave(self,e):
            if self.password.get() == "":
                self.password.insert(0, "Password")

    def p_enter(self,e):
            self.password.delete(0, "end")

        

        
        
    


#definition of the function for signup




class signin:
    def __init__(self, window):
        self.window = window
        def on_enter(self):
            self.username.delete(0, "end")

        def on_leave(self,e):
            if self.username.get() == "":
                self.username.insert(0, "Username")

        def p_leave(self):
            if self.password.get() == "":
                self.password.insert(0, "Password")

        def p_enter(self):
            self.password.delete(0, "end")
    
        self.window.geometry("925x500+300+200")
        self.window.configure(bg="#fff")
        self.window.resizable(True, True)
        self.window.title("Sign up")
    

        self.frame = Frame(self.window, width=350, height=390, bg="#fff")
        self.frame.place(x=480, y=50)

        self.sign_uplabel = Label(self.frame, text="Sign In ", fg="#57a1f8", bg="White",
                             font=("Microsoft Yahei UI Light", 23, "bold"))
        self.sign_uplabel.place(x=100, y=5)
        self.username = Entry(self.frame, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
        self.username.place(x=80, y=80)
        Frame(self.frame, width=295, height=2, bg="black").place(x=80, y=107)
        self.username.insert(0, "Username")
        self.username.bind("<FocusIn>", on_enter)
        self.username.bind("<FocusOut>", on_leave)

        self.password = Entry(self.frame, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
        self.password.place(x=80, y=140)
        Frame(self.frame, width=295, height=2, bg="black").place(x=80, y=167)
        self.password.insert(0, "Password")
        self.password.bind("<FocusIn>", p_enter)
        self.password.bind("<FocusOut>", p_leave)

        self.user_create = Button(self.frame, width=20, pady=2, text="Sign in", bg="#57a1f8", fg="white", border=0,
               font=("Microsoft Yahei UI Light", 11))
        self.user_create.place(x=80, y=200)
        self.account_havelabel = Label(self.frame, text="I don't an account", fg="#57a1f8", bg="White",
                                  font=("Microsoft Yahei UI Light", 11))
        self.account_havelabel.place(x=80, y=240)

        self.signup_button = Button(self.frame, width=20, pady=2, text="Sign up", bg="#57a1f8", fg="white", border=0,
                               font=("Microsoft Yahei UI Light", 11))
        self.signup_button.place(x=80, y=280)
        
    

window1 = Tk()

w = signin(window1)


mainloop()





