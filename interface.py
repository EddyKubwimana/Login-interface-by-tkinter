#employees class
import pandas as pd
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

class accountant(agent):
    
    def __init__(self,Id, fname, sname, location, phone, capital, employees = None):
        super().__init__(Id, fname, sname, location, phone, capital)
        if employees == None:
            self.employees = [employees]
        else:
            self.employees = employees
                  
    def get_employees(self, employees):
        ids = []
        names =[]
        locations =[]
        phones = []
        capitals =[]
        for i in employees:
            ids.append(i.Id)
            names.append(i.sname)
            locations.append(i.location)
            phones.append(i.phone)
            capitals.append(i.capital)
        
        
    
        result= pd.DataFrame({"Name":names,
                              "Location" : locations,
                              "Tel" : phones,
                              "Capital amount" : capitals}, index = ids)
        return result
        
        

        
    

m1 = manager(8309, "eddy", "kubwimana", "Shombo", 51578, 800000)
m2 = agent(8307, "eddy", "kubwimana", "Shombo", 51578900, 800000)
m3 = accountant(8308, "eddy", "kubwimana", "Shombo", 51578900, 800000)
m4 = manager(8306, "eddy", "kubwimana", "Shombo", 515789, 800000)
m5 = accountant(8304, "eddy", "kubwimana", "Shombo", 51578900, 800000)
m6 = manager(8305, "eddy", "kubwimana", "Shombo", 51500, 800000)
m7 = agent(8303, "eddy", "kubwimana", "Shombo", 51578900, 800000)

employees = [m1,m2,m3,m4,m5,m6,m7]

employees_rapport = m5.get_employees(employees)
print(employees_rapport)




