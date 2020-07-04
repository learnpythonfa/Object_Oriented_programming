class Student:
    def __init__(self,fname,lname,score):
        # initializing the variables inside the Student class
        self.fname = fname # first name
        self.lname = lname # last name
        self.testScore = score # test score
        self.fullname = fname+","+lname


objStudent_1 = Student("John","Legend",95)
objStudent_2 = Student("Rose","schmitt",86)

print("ObjStudent_1: fullname",objStudent_1.fullname,"score",objStudent_1.testScore)
print("ObjStudent_2: fullname",objStudent_2.fullname,"score",objStudent_2.testScore)
