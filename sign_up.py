from tkinter import *
from tkinter import messagebox
import ast
import sqlite3 as sq
import sign_in
# the whole sign up form           
class signup:
    def __init__(self,sq):
        self.window = Tk()
        self.window.withdraw()
        self.window = Toplevel()
        self.sq = sq
        self.db = self.sq.connect("Agent-Connect.db")
        self.cursor = self.db.cursor()
        self.window.geometry("925x500+100+3")
        self.window.configure(bg ="#fff")
        self.window.resizable(True, True)
        self.image =PhotoImage(file = "logo.png")
        Label(self.window, image = self.image, border = 0, bg = "white").place ( x =5, y = 90)
        self.frame1= Frame (self.window, width = 350, height = 390 , bg = "#fff")
        self.frame1.place(x =480, y = 50)


        self.sign_uplabel = Label(self.frame1, text = "SignUp", fg = "#57a1f8", bg = "White", font = ( "Microsoft Yahei UI Light", 23, "bold"))
        self.sign_uplabel.place(x = 100, y = 5)
        self.window.title("Sign up")

        self.username = Entry(self.frame1 ,width = 25, border = 0 ,fg = "black", bg = "white", font = ( "Microsoft Yahei UI Light", 11))
        self.username.place(x = 80, y = 80)
        Frame(self.frame1 , width =295 , height = 2, bg = "black").place(x = 80, y = 107)
        self.username.insert(0, "Username")
        self.username.bind("<FocusIn>", self.name_enter)
        self.username.bind("<FocusOut>", self.name_leave)

        
        self.password = Entry(self.frame1 ,width = 25, border = 0 ,fg = "black", bg = "white", font = ( "Microsoft Yahei UI Light", 11))
        self.password.place(x = 80, y = 140)
        Frame(self.frame1 , width =295 , height = 2, bg = "black").place(x = 80, y = 167)
        self.password.insert(0, "Password")
        self.password.bind("<FocusIn>", self.p_enter)
        self.password.bind("<FocusOut>", self.p_leave)


        
        self.confirm_password = Entry(self.frame1 ,width = 25, border = 0 ,fg = "black", bg = "white", font = ( "Microsoft Yahei UI Light", 11))
        self.confirm_password.place(x = 80, y = 200)
        Frame(self.frame1 , width =295 , height = 2, bg = "black").place(x = 80, y = 227)
        self.confirm_password.insert(0,"confirm password")
        self.confirm_password.bind("<FocusIn>", self.cp_enter)
        self.confirm_password.bind("<FocusOut>", self.cp_leave)

        #sign up Button
        Button( self.frame1, width = 20, pady = 2, text = "Sign up", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 11),command = self.b_up).place( x = 80, y = 260)
        self.account_havelabel = Label(self.frame1, text = "I have an account", fg = "#57a1f8", bg = "White", font = ( "Microsoft Yahei UI Light", 11))
        self.account_havelabel.place(x= 80, y = 300)

        self.signin_button = Button( self.frame1, width = 20, pady = 2, text = "Sign in", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 11),
                                     command = lambda :[sign_in.S_in(),self.destroy()])
        self.signin_button.place(x=80, y = 340)
    # user confirm password event

    def cp_enter(self,e):
        self.confirm_password.delete(0,"end")
        self.confirm_password.config(show ="*")
    def cp_leave(self,e):
        if self.confirm_password.get() == "":
            self.confirm_password.config(show ="")
            self.confirm_password.insert(0, "confirm_password")
                    
    # user password validation event
    def p_enter(self,e):
        self.password.delete(0,"end")
        self.password.config(show ="*")
    def p_leave(self,e):
        if self.password.get() == "":
            self.password.config(show = "")
            self.password.insert(0, "password")
    #user username entry event
    def name_enter(self,e):
        self.username.delete(0,"end")
            
    def  name_leave(self,e):
        if self.username.get() == "":
            self.username.insert(0, "Username")
    #function to destroy this object once user switches windows
    def destroy(self):
        self.window.destroy()
    
    #function to validate the login  creadentials
    def b_up(self):
        
        usernam = str(self.username.get())
        passwor = int(self.password.get())
        cp_confirm = int(self.confirm_password.get())
        if passwor == cp_confirm:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS user([username] TEXT PRIMARY KEY, [password] INTEGER)')
            self.cursor.execute(f'INSERT INTO user(username,password) VALUES ("{usernam}", "{passwor}")')
            self.db.commit()
            messagebox.showinfo('signed up successfully', 'Welcome to Agent-Connect')
        else:
           messagebox.showinfo('password error','Password do not match')
            

      
#function to call the class object
def up():
    signup(sq)
