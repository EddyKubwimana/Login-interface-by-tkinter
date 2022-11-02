from tkinter import *
from tkinter import messagebox
import ast
window =Tk()
window.title("Sign up")
window.geometry("925x500+300+200")
window.configure(bg ="#fff")
window.resizable(False, True)
image = PhotoImage(file = "logo.png")
Label(window, image = image, border = 0, bg = "white").place ( x =5, y = 90)
frame = Frame (window, width = 350, height = 390 , bg = "#fff")
frame.place(x =480, y = 50)
sign_uplabel = Label(frame, text = "SignUp", fg = "#57a1f8", bg = "White", font = ( "Microsoft Yahei UI Light", 23, "bold"))
sign_uplabel.place(x = 100, y = 5)

#sign up Button
def signup():
    username = username.get()
    password= password.get()
    confirm_password = confirm_passord.get()
    if password == confirm_password:





# user entry

def on_enter(e):
    username.delete(0,"end")
def on_leave(e):
    if username.get() == "":
        username.insert(0, "Username")
username = Entry(frame ,width = 25, border = 0 ,fg = "black", bg = "white", font = ( "Microsoft Yahei UI Light", 11))
username.place(x = 80, y = 80)
Frame(frame , width =295 , height = 2, bg = "black").place(x = 80, y = 107)
username.insert(0, "Username")
username.bind("<FocusIn>", on_enter)
username.bind("<FocusOut>", on_leave)

#user_password

def on_enter(e):
    password.delete(0,"end")
def on_leave(e):
    if password.get() == "":
        password.insert(0, "Password")
password = Entry(frame ,width = 25, border = 0 ,fg = "black", bg = "white", font = ( "Microsoft Yahei UI Light", 11))
password.place(x = 80, y = 140)
Frame(frame , width =295 , height = 2, bg = "black").place(x = 80, y = 167)
password.insert(0, "Password")
password.bind("<FocusIn>", on_enter)
password.bind("<FocusOut>", on_leave)


#password confirmation

def enter(e):
    confirm_password.delete(0,"end")
def leave(e):
    if confirm_password.get() == "":
        confirm_password.insert(0, "Confirm password")
confirm_password = Entry(frame ,width = 25, border = 0 ,fg = "black", bg = "white", font = ( "Microsoft Yahei UI Light", 11))
confirm_password.place(x = 80, y = 200)
Frame(frame , width =295 , height = 2, bg = "black").place(x = 80, y = 227)
confirm_password.insert(0, "Confirm password")
confirm_password.bind("<FocusIn>", enter)
confirm_password.bind("<FocusOut>", leave)

#sign up Button
Button( frame, width = 20, pady = 2, text = "Sign up", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 11), command = signup ).place( x = 80, y = 260)
account_havelabel = Label(frame, text = "I have an account", fg = "#57a1f8", bg = "White", font = ( "Microsoft Yahei UI Light", 11))
account_havelabel.place(x= 80, y = 300)

signin_button = Button( frame, width = 20, pady = 2, text = "Sign in", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 11) )
signin_button.place(x=80, y = 340)


#sign in window

def us_enter(e):
    username.delete(0,"end")
def us_leave(e):
    if username.get() == "":
        username.insert(0, "Username")
username = Entry(frame ,width = 25, border = 0 ,fg = "black", bg = "white", font = ( "Microsoft Yahei UI Light", 11))
username.place(x = 80, y = 80)
Frame(frame , width =295 , height = 2, bg = "black").place(x = 80, y = 107)
username.insert(0, "Username")
username.bind("<FocusIn>", us_enter)
username.bind("<FocusOut>", us_leave)

#user_password

def p_enter(e):
    password.delete(0,"end")
def p_leave(e):
    if password.get() == "":
        password.insert(0, "Password")
password = Entry(frame ,width = 25, border = 0 ,fg = "black", bg = "white", font = ( "Microsoft Yahei UI Light", 11))
password.place(x = 80, y = 140)
Frame(frame , width =295 , height = 2, bg = "black").place(x = 80, y = 167)
password.insert(0, "Password")
password.bind("<FocusIn>", p_enter)
password.bind("<FocusOut>", p_leave)

#sign up Button
Button( frame, width = 20, pady = 2, text = "Sign in", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 11), command = signup ).place( x = 80, y = 200)
account_havelabel = Label(frame, text = "I don't an account", fg = "#57a1f8", bg = "White", font = ( "Microsoft Yahei UI Light", 11))
account_havelabel.place(x= 80, y = 240)

signin_button = Button( frame, width = 20, pady = 2, text = "Sign up", bg = "#57a1f8", fg = "white", border = 0,font = ( "Microsoft Yahei UI Light", 11) )
signin_button.place(x=80, y = 340)





window.mainloop
