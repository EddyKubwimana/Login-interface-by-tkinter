#employees class

class agent:
    def __init__(self, Id, fname, sname, location, phone, capital):
        self.Id = Id
        self.fname = fname
        self.sname = sname
        self.location = location
        self.phone = phone
        self.capital = capital
    @property
    def profile(self):
        return f"Id: {str(self.Id)}" + " "+f"{self.fname}"+" " +f"{self.sname}"+ " "+ f"telephone : {str(self.phone)}"+ " " +f"works at { self.location}"+ " " + f"with {str(self.capital)} BIF" 
    def __str__(self):
        return f"Id: {str(self.Id)}" + " "+f"{self.fname}"+" " +f"{self.sname}"+ " "+ f"telephone : {str(self.phone)}"+ " " +f"works at { self.location}"+ " " + f"with {str(self.capital)} BIF" 

class manager(agent):
    def __init__(self, Id, fname, sname, location, phone, capital, underline= None):
        super().__init__(Id, fname, sname, location, phone, capital)
        if underline == None:
            
             self.underline = []
        else:
            self.underline = [underline]

    def add_underline(self, name):
        self.underline.append(name)

    def remove_underline(self, name):
        self.underline.remove(name)
        
    

m1 = manager(8309, "eddy", "kubwimana", "Shombo", 51578900, 800000)

