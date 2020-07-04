
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

# Inherits
class Instructor(Person):
    #raise amount instructor
    raise_amt = 1.01
    pass

objInstructor_1  = Instructor("adam","burg",35)
objInstructor_2  = Instructor("rita","algor",31)

print(objInstructor_1)
print(objInstructor_2)