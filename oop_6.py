
class Person:
    # class variable 
    raise_amt = 1.05 # annual raise percentage
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def increase_pay(self):
        self.pay = self.pay * self.raise_amt
    def __repr__(self):
        return "%s pay:%f"%(self.fname+self.lname,self.pay)

# Inherits from Person
class Instructor(Person):
    #raise amount instructor
    raise_amt = 1.01
    def __init__(self,fname,lname, pay,teaching_specialty):
        super().__init__(fname,lname,pay)
        self.teaching_specialty = teaching_specialty


objInstructor_1  = Instructor("adam","burg",35,"python")
objInstructor_2  = Instructor("rita","algor",31,"math")

print(objInstructor_1.teaching_specialty)
print(objInstructor_2.teaching_specialty)