#Class & Object in Python

class Students:
    collage_name = 'BCAS'   #Class variable / class attributes
    fullname = 'anonymus'
    def __init__(self, fullname ,lastname,age):
        self.fullname = fullname  #instances attributes
        self.lastname = lastname  #instances attributes
        self.age = age
    def welcome(self):
        return  self.fullname

    def change_collage_name(self,new_name):    #Class method
        Students.collage_name = new_name

s1 = Students('pranjal','mourya',28 )
print(s1.fullname,s1.lastname,s1.age,s1.collage_name)

s2 = Students('Krant','mourya',33) 
print('Welcome!', s2.welcome(),s2.fullname,s2.lastname,s2.age,s2.collage_name)


s3 = Students('Ritu','mourya',24)
s3.change_collage_name('MGKV') 
print(s1.fullname,s1.lastname,s1.age,s1.collage_name)

s4 = Students(Students.fullname,'mourya',33)
print(s3.welcome(),'! ',s3.fullname,s3.lastname,s3.age,s3.collage_name)





