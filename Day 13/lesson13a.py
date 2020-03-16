class Person():
    
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
       

    def getdata(self):
        data = str(self.id) + " " + self.name + " " + self.salary
        return data

class Employee(Person):
    
    def __init__(self,id,name,salary,email):
        super().__init__(id,name,salary)
        self.email= email

    def getdata(self):
        data = str(self.id) + " " + self.name + " " + str(self.salary) + " " + self.email
        return data
        
emp = Employee(1,'Yeasin',1 ,'gdahgd@ffhsk.com')
print(emp.getdata())