
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

class Manager(Person):
    def __init__(self,fname,lname, pay,employee_list=None):
        super().__init__(fname,lname,pay)
        if employee_list is None:
            self.employee_list = []
        else:
            self.employee_list = employee_list
    # add instructor
    def add_instructor(self,instructor):
        if instructor not in self.employee_list:
            self.employee_list.append(instructor)
    #removes instructor
    def remove_instructor(self,instructor):
        if instructor in self.employee_list:
            self.employee_list.remove(instructor)
    
    def print_instructors(self):
        print('list of employees for %s'%self.fname)
        for inst in self.employee_list:
            print(inst.fname)


# Inherits from Person
class Instructor(Person):
    #raise amount instructor
    raise_amt = 1.01
    def __init__(self,fname,lname, pay,teaching_specialty):
        super().__init__(fname,lname,pay)
        self.teaching_specialty = teaching_specialty


objInstructor_1  = Instructor("adam","burg",37,"python")
objInstructor_2  = Instructor("rita","algor",31,"math")
objInstructor_3  = Instructor("John","Baptist",35,"physics")
objInstructor_4  = Instructor("Greg","Joe",29,"chemical")

print(objInstructor_1.teaching_specialty)
print(objInstructor_2.teaching_specialty)
print(objInstructor_3.teaching_specialty)
print(objInstructor_4.teaching_specialty)

objManager_1 = Manager("david","Copper",56,[objInstructor_1,objInstructor_2])
objManager_1.print_instructors()
objManager_1.add_instructor(objInstructor_3)
objManager_1.print_instructors()
objManager_1.remove_instructor(objInstructor_1)
objManager_1.print_instructors()

objManager_2 = Manager("Rick","Chal",56)
objManager_2.print_instructors()
objManager_2.add_instructor(objInstructor_1)
objManager_2.print_instructors()


