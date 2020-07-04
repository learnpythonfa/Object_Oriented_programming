
class Student:
    def __init__(self,fname,lname,score):
        # initializing the variables inside the Student class
        self.fname = fname # first name
        self.lname = lname # last name
        self.testScore = score # test score
        self.fullname = fname+","+lname

    def __repr__(self):
        return "Student Name %s, score: %d"%(self.fullname, self.testScore)

    def getFullname (self):
        return self.fname+","+self.lname

    def status(self):
        print(self.fullname,"score:",self.testScore)

objStudent_1 = Student("John","Legend",95)
objStudent_2 = Student("Rose","schmitt",86)

# print(objStudent_1.getFullname() )
# print(objStudent_1.status())

print(objStudent_1)
print(objStudent_2)