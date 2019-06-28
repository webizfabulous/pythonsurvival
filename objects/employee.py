#AN employee class with __init__


class Employee:

    def __init__(self, name,address,salary):
        self.name = name  #string
        self.address = address #string
        self.salary =salary #int

    def __str__(self): 
        #str should always return a value
        return (f"( {self.name} , {self.address} , {self.salary} )")


emp1 = Employee('samman' , 'chitwan' ,11)
print(emp1) #it will automatically call __str__ method



