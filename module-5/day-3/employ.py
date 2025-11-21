class Person:
    
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name, self.idnumber)
        
class Employee(Person):
    
    def __init__(self, salary, post, name, idnumber):
        self.salary = salary
        self.post = post
        
        super().__init__(name, idnumber)
    def display(self):
        print(self.name, self.idnumber, self.salary, self.post)
a = Employee(20000, "Intern", "Liam", 17800)
a.display()