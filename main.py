from tkinter import *
import cv2
from tkinter import messagebox
import ast


# sign up from
def sign_up():

    frame1 = Frame(window1, width=350, height=390, bg="#fff")
    frame1.place(x=480, y=50)

    def on_enter(e):
        username.delete(0, "end")

    def on_leave(e):
        if username.get() == "":
            username.insert(0, "Username")

    # user confirm password

    def cp_enter(e):
        confirm_password.delete(0, "end")

    def cp_leave(e):
        if confirm_password.get() == "":
            confirm_password.insert(0, "Confirm password")

    def p_leave(e):
        if password.get() == "":
            password.insert(0, "Password")

    def p_enter(e):
        password.delete(0, "end")

    sign_uplabel = Label(frame1, text="SignUp", fg="#57a1f8", bg="White", font=("Microsoft Yahei UI Light", 23, "bold"))
    sign_uplabel.place(x=100, y=5)

    username = Entry(frame1, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    username.place(x=80, y=80)
    Frame(frame1, width=295, height=2, bg="black").place(x=80, y=107)
    username.insert(0, "Username")
    username.bind("<FocusIn>", on_enter)
    username.bind("<FocusOut>", on_leave)

    password = Entry(frame1, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    password.place(x=80, y=140)
    Frame(frame1, width=295, height=2, bg="black").place(x=80, y=167)
    password.insert(0, "Password")
    password.bind("<FocusIn>", p_enter)
    password.bind("<FocusOut>", p_leave)

    confirm_password = Entry(frame1, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    confirm_password.place(x=80, y=200)
    Frame(frame1, width=295, height=2, bg="black").place(x=80, y=227)
    confirm_password.insert(0, "Confirm password")
    confirm_password.bind("<FocusIn>", cp_enter)
    confirm_password.bind("<FocusOut>", cp_leave)

    # sign up Button
    Button(frame1, width=20, pady=2, text="Sign up", bg="#57a1f8", fg="white", border=0,
           font=("Microsoft Yahei UI Light", 11)).place(x=80, y=260)
    account_havelabel = Label(frame1, text="I have an account", fg="#57a1f8", bg="White",
                              font=("Microsoft Yahei UI Light", 11))
    account_havelabel.place(x=80, y=300)

    signin_button = Button(frame1, width=20, pady=2, text="Sign in", bg="#57a1f8", fg="white", border=0,
                           font=("Microsoft Yahei UI Light", 11), command=signin_form)
    signin_button.place(x=80, y=340)


def signin_form():

    def on_enter(e):
        username.delete(0, "end")

    def on_leave(e):
        if username.get() == "":
            username.insert(0, "Username")

    def p_leave(e):
        if password.get() == "":
            password.insert(0, "Password")

    def p_enter(e):
        password.delete(0, "end")

    frame2 = Frame(window1, width=350, height=390, bg="#fff")
    frame2.place(x=480, y=50)

    sign_uplabel = Label(frame2, text="Sign In ", fg="#57a1f8", bg="White",
                         font=("Microsoft Yahei UI Light", 23, "bold"))
    sign_uplabel.place(x=100, y=5)
    username = Entry(frame2, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    username.place(x=80, y=80)
    Frame(frame2, width=295, height=2, bg="black").place(x=80, y=107)
    username.insert(0, "Username")
    username.bind("<FocusIn>", on_enter)
    username.bind("<FocusOut>", on_leave)

    password = Entry(frame2, width=25, border=0, fg="black", bg="white", font=("Microsoft Yahei UI Light", 11))
    password.place(x=80, y=140)
    Frame(frame2, width=295, height=2, bg="black").place(x=80, y=167)
    password.insert(0, "Password")
    password.bind("<FocusIn>", p_enter)
    password.bind("<FocusOut>", p_leave)

    Button(frame2, width=20, pady=2, text="Sign in", bg="#57a1f8", fg="white", border=0,
           font=("Microsoft Yahei UI Light", 11)).place(x=80, y=200)
    account_havelabel = Label(frame2, text="I don't an account", fg="#57a1f8", bg="White",
                              font=("Microsoft Yahei UI Light", 11))
    account_havelabel.place(x=80, y=240)

    signup_button = Button(frame2, width=20, pady=2, text="Sign up", bg="#57a1f8", fg="white", border=0,
                           font=("Microsoft Yahei UI Light", 11), command=sign_up)
    signup_button.place(x=80, y=280)

window1 = Tk()
window1.geometry("925x500+300+200")
window1.configure(bg="#fff")
window1.resizable(True, True)
window1.title("Sign up")
sign_up()

mainloop()





