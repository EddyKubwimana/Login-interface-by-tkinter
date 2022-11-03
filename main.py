from tkinter import *
import cv2
from tkinter import messagebox
import ast

window = Tk()

window.geometry("925x500+300+200")
window.configure(bg="#fff")
window.resizable(True, True)
image = PhotoImage(file="logo.png")
Label(window, image=image, border=0, bg="white").place(x=5, y=90)


# user entry

def on_enter(username):
    print(username.delete(0, "end"))


def on_leave(username):
    if username.get() == "":
        return username.insert(0, "Username")


# user confirm password

def enter(confirm_password):
    return confirm_password.delete(0, "end")


def leave(confirm_password):
    if confirm_password.get() == "":
        return confirm_password.insert(0, "Confirm password")


# user password validation
def on_enter(password):
    return password.delete(0, "end")


def on_leave(password):
    if password.get() == "":
        return password.insert(0, "Password")


def us_enter(username):
    return username.delete(0, "end")


def us_leave(username):
    if username.get() == "":
        return username.insert(0, "Username")


def p_enter(password):
    return password.delete(0, "end")


def p_leave(password):
    if password.get() == "":
        return password.insert(0, "Password")


# sign up from

def signup_form():
    # sign up Button
    frame1 = Frame(window, width=350, height=390, bg="#fff")
    frame1.place(x=480, y=50)

    sign_uplabel = Label(frame1, text="SignUp", fg="#57a1f8", bg="White", font=("Microsoft Yahei UI Light", 23, "bold"))
    sign_uplabel.place(x=100, y=5)
    window.title("Sign up")

    username = Entry(frame1, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    username.place(x=80, y=80)
    Frame(frame1, width=295, height=2, bg="black").place(x=80, y=107)
    username.insert(0, "Username")
    username.bind("<FocusIn>", on_enter(username))
    username.bind("<FocusOut>", on_leave(username))

    password = Entry(frame1, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    password.place(x=80, y=140)
    Frame(frame1, width=295, height=2, bg="black").place(x=80, y=167)
    password.insert(0, "Password")
    password.bind("<FocusIn>", on_enter(password))
    password.bind("<FocusOut>", on_leave(password))

    confirm_password = Entry(frame1, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    confirm_password.place(x=80, y=200)
    Frame(frame1, width=295, height=2, bg="black").place(x=80, y=227)
    confirm_password.insert(0, "Confirm password")
    confirm_password.bind("<FocusIn>", enter(confirm_password))
    confirm_password.bind("<FocusOut>", leave(confirm_password))

    # sign up Button
    Button(frame1, width=20, pady=2, text="Sign up", bg="#57a1f8", fg="white", border=0,
           font=("Microsoft Yahei UI Light", 11)).place(x=80, y=260)
    account_havelabel = Label(frame1, text="I have an account", fg="#57a1f8", bg="White",
                              font=("Microsoft Yahei UI Light", 11))
    account_havelabel.place(x=80, y=300)

    signin_button = Button(frame1, width=20, pady=2, text="Sign in", bg="#57a1f8", fg="white", border=0,
                           font=("Microsoft Yahei UI Light", 11), command=lambda: signin_form())
    signin_button.place(x=80, y=340)


def signin_form():
    window.title("Sign in")
    frame2 = Frame(window, width=350, height=390, bg="#fff")
    frame2.place(x=480, y=50)

    sign_uplabel = Label(frame2, text="Sign In ", fg="#57a1f8", bg="White",
                         font=("Microsoft Yahei UI Light", 23, "bold"))
    sign_uplabel.place(x=100, y=5)
    username = Entry(frame2, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    username.place(x=80, y=80)
    Frame(frame2, width=295, height=2, bg="black").place(x=80, y=107)
    username.insert(0, "Username")
    username.bind("<FocusIn>", us_enter(username))
    username.bind("<FocusOut>", us_leave(username))

    password = Entry(frame2, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    password.place(x=80, y=140)
    Frame(frame2, width=295, height=2, bg="black").place(x=80, y=167)
    password.insert(0, "Password")
    password.bind("<FocusIn>", p_enter(password))
    password.bind("<FocusOut>", p_leave(password))

    Button(frame2, width=20, pady=2, text="Sign in", bg="#57a1f8", fg="white", border=0,
           font=("Microsoft Yahei UI Light", 11)).place(x=80, y=200)
    account_havelabel = Label(frame2, text="I don't an account", fg="#57a1f8", bg="White",
                              font=("Microsoft Yahei UI Light", 11))
    account_havelabel.place(x=80, y=240)

    signup_button = Button(frame2, width=20, pady=2, text="Sign up", bg="#57a1f8", fg="white", border=0,
                           font=("Microsoft Yahei UI Light", 11), command=lambda: signup_form())
    signup_button.place(x=80, y=280)


def options():
    dataOptions = ["New", "open", "Save", "Save as"]
    dataOptionsAfterseparator = ["Import", "Export", "Exit"]
    viewOptions = ["Transform", "Edit", "Create"]
    menuBar = Menu(window)
    file = Menu(menuBar, tearoff=0)
    for i in dataOptions:
        file.add_command(label=i, command=None)
    file.add_separator()
    for i in dataOptionsAfterseparator:
        file.add_command(label=i, command=None)
    menuBar.add_cascade(label="File", menu=file)
    View = Menu(menuBar, tearoff=0)
    for i in viewOptions:
        View.add_command(label=i, command=None)
    menuBar.add_cascade(label="View", menu=View)
    window.config(menu=menuBar)


signin_form()

window.mainloop
