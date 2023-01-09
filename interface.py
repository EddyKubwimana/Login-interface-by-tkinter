#employees class
import pandas as pd
import time
class Agent:
    def __init__(self, Id, fname, sname, location, phone, capital):
        self.Id = Id
        self.fname = fname
        self.sname = sname
        self.location = location
        self.phone = phone
        self.capital = capital
    @property
    def profile(self):
        '''return the profile of the agent'''
    
        return f"Id: {str(self.Id)}" + " "+f"{self.fname}"+" " +f"{self.sname}"+ " "+ f"telephone : {str(self.phone)}"+ " " +f"works at { self.location}"+ " " + f"with {str(self.capital)} BIF" 
    def __str__(self):
        '''special method when someone print the function'''
        
        return f"Id: {str(self.Id)}" + " "+f"{self.fname}"+" " +f"{self.sname}"+ " "+ f"telephone : {str(self.phone)}"+ " " +f"works at { self.location}"+ " " + f"with {str(self.capital)} BIF" 

class Manager(Agent):
    def __init__(self, Id, fname, sname, location, phone, capital, underline= None):
        super().__init__(Id, fname, sname, location, phone, capital)
        if underline == None:
            
             self.underline = []
        else:
            self.underline = [underline]

    def add_underline(self, name):
        '''add a a new agent under a a manager'''
        self.underline.append(name)

    def remove_underline(self, name):
        '''add an underline under the manager'''
        
        self.underline.remove(name)

class Accountant(Agent):
    
    def __init__(self,Id, fname, sname, location, phone, capital, employees = None):
        super().__init__(Id, fname, sname, location, phone, capital)
        if employees == None:
            self.employees = [employees]
        else:
            self.employees = employees
                  
    def get_employees(self, employees):
        ''' return the names of all employees in a company'''
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
        

class Income:
    def __init__(self, IncomeId, amount, agent_id,date = None):
        self.IncomeId = income.IncomeId
        self.amount = amount
        self.agent_id = agent_id
        if date == None:
            self.date = time.now()
        self.date = asctime()

    def get_details(self, IncomeId):

        if self.IncomeId == IncomeId:
            pass
            
        



    





