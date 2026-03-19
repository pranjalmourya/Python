'''Create student class that name and marks of 3 subjects as arguments in constructor. Then create a method to print the averge'''

class students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum = 0    
            sum += i
        print(self.name,' got ',sum/3, ' marks')
    @staticmethod  
    def hellow():
        print('Hellow')    
        
s1 = students('pranjal',[98,85,81])    

s1.get_avg()
s1.name = 'Ritu'
s1.marks = [40,50,45,]
s1.get_avg()
s1.hellow()
