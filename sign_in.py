from tkinter import *
from tkinter import messagebox
import ast
import sign_up

class SignIn:
    def __init__(self, window):
        self.window = window
        self.window.title("Sign in")
        self.window.geometry("925x500+100+3")
        self.window.configure(bg ="#fff")
        self.window.resizable(True, True)
        #self.image = PhotoImage(file = "logo.png")
        #Label(self.window, image = self.image, border = 0, bg = "white").place ( x =5, y = 90)
    
    
        self.frame = Frame (self.window, width = 350, height = 390 , bg = "#fff")
        self.frame.place(x =480, y = 50)


        self.sign_uplabel = Label(self.frame, text = "Sign In ", fg = "#57a1f8", bg = "White", font = ( "Microsoft Yahei UI Light", 23, "bold"))
        self.sign_uplabel.place(x = 100, y = 5)
        self.username = Entry(self.frame ,width = 25, border = 0 ,fg = "black", bg = "white", font = ( "Microsoft Yahei UI Light", 11))
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


        Button( self.frame, width = 20, pady = 2, text = "Sign in", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 11) ).place( x = 80, y = 200)
        self.account_havelabel = Label(self.frame, text = "I don't an account", fg = "#57a1f8", bg = "White", font = ( "Microsoft Yahei UI Light", 11))
        self.account_havelabel.place(x= 80, y = 240)

        self.signup_button = Button( self.frame, width = 20, pady = 2, text = "Sign up", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 11),
                                     command = lambda:[self.destroy(),sign_up.up()])
        self.signup_button.place(x=80, y = 280)
    def get_id(self):
        print(self.username.get())
        print(self.password.get())
        self.window.mainloop
    def name_enter(self,e):
        self.username.delete(0,"end")
    
    def name_leave(self,e):
        if self.username.get() == "":
             self.username.insert(0, "Username")
                    
    def p_enter(self,e):
        self.password.delete(0,"end")
                
    def p_leave(self,e):
        if self.password.get() == "":
            self.password.insert(0, "Password")

    def destroy(self):
        self.window.destroy()



def S_in():
    window =Tk()
    form = SignIn(window)



