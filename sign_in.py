from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
import ast
import sign_up

#sign in form
class SignIn:
    def __init__(self, sq):
        self.window = Tk()
        self.window.withdraw()
        self.window = Toplevel()
        self.sq = sq
        self.db = self.sq.connect('Agent-Connect.db')
        self.cursor = self.db.cursor()
        self.window.title("Sign in")
        self.window.geometry("925x500+100+3")
        self.window.configure(bg ="#fff")
        self.window.resizable(True, True)
        self.image = PhotoImage(file = "logo.png")
        Label(self.window, image = self.image, border = 0, bg = "white").place ( x =5, y = 90)
    
    
        self.frame = Frame (self.window, width = 350, height = 390 , bg = "#fff")
        self.frame.place(x =480, y = 50)


        self.sign_uplabel = Label(self.frame, text = "Sign In ", fg = "#57a1f8", bg = "White", font = ( "Microsoft Yahei UI Light", 23, "bold"))
        self.sign_uplabel.place(x = 100, y = 5)
        self.username = Entry(self.frame,width = 25, border = 0 ,fg = "black", bg = "white", font = ( "Microsoft Yahei UI Light", 11))
        self.username.place(x = 80, y = 80)
        Frame(self.frame , width =295 , height = 2, bg = "black").place(x = 80, y = 107)
        self.username.insert(0, "Username")
        self.username.bind("<FocusIn>",self.name_enter )
        self.username.bind("<FocusOut>",self.name_leave)

        
        self.password = Entry(self.frame ,width = 25, border = 0 ,fg = "black", bg = "white", font = ( "Microsoft Yahei UI Light", 11))
        self.password.place(x = 80, y = 140)
        Frame(self.frame , width =295 , height = 2, bg = "black").place(x = 80, y = 167)
        self.password.insert(0, "Password")
        self.password.bind("<FocusIn>",self.p_enter )
        self.password.bind("<FocusOut>",self.p_leave)


        Button( self.frame, width = 20, pady = 2, text = "Sign in", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 11),command = self.sign_ ).place( x = 80, y = 200)
        self.account_havelabel = Label(self.frame, text = "I don't an account", fg = "#57a1f8", bg = "White", font = ( "Microsoft Yahei UI Light", 11))
        self.account_havelabel.place(x= 80, y = 240)

        self.signup_button = Button( self.frame, width = 20, pady = 2, text = "Sign up", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 11),
                                     command = lambda:[self.destroy(),sign_up.up()])
        self.signup_button.place(x=80, y = 280)

    #event that happens when the cursor is inside the username entry
    def name_enter(self,e):
        self.username.delete(0,"end")

    #Event when the user leaves username entry
    def name_leave(self,e):
        if self.username.get() == "":
             self.username.insert(0, "Username")
    #event when the cursor is inside the password entry             
    def p_enter(self,e):
        self.password.delete(0,"end")
        self.password.config(show = "*")
    #event when the user leaves the password entry         
    def p_leave(self,e):
        if self.password.get() == "":
            self.password.config(show = "")
            self.password.insert(0, "Password")
    #function to destroy the whole object
    def destroy(self):
        self.window.destroy()

    def sign_(self):
        usernam = self.username.get()
        credential = self.cursor.execute(f'SELECT username, password FROM user where username= "{usernam}"')
        credential = credential.fetchall()
        if len(credential)==0:
            messagebox.showerror('Sorry', 'The user does not exist')
        else:
            if int(self.password.get()) == int(credential[0][1]):
                messagebox.showinfo('Successfully connected', 'Welcome back to the team')
                                  
        


#Function to call the sign in object
def S_in():
   SignIn(sq)

