def name_enter(e):
    username.delete(0,"end")
    
def name_leave(e):
    if username.get() == "":
         username.insert(0, "Username")
                
def p_enter(e):
    password.delete(0,"end")
            
def p_leave(e):
    if password.get() == "":
        password.insert(0, "Password")
