import datetime

class Student:
    # class variable 
    number_of_question = 100
    number_of_students = 0
    def __init__(self,fname,lname,score):
        # initializing the variables inside the Student class
        self.fname = fname # first name
        self.lname = lname # last name
        self.testScore = score # test score
        self.fullname = fname+","+lname
        # calss variable
        Student.number_of_students +=1 

    def __repr__(self):
        return "Student Name %s, score: %d"%(self.fullname, self.testScore)

    def getFullname (self):
        return self.fname+","+self.lname
    def calculate_score_percentatge(self):
        return (self.testScore/self.number_of_question)
    
    @classmethod # decorative
    def change_number_of_questions(cls,number_of_question):
        cls.number_of_question = number_of_question
    
    @staticmethod # static method
    def is_workday(day):
        if day.weekday()>=0 and day.weekday()<5:
            return True
        else:
            return False
    
# using the static method
my_workday = datetime.date(2020,7,4)
print(my_workday.weekday())
print(Student.is_workday(my_workday))


objStudent_1 = Student("John","Legend",95)
print(Student.number_of_students)

objStudent_2 = Student("Rose","schmitt",86)
# print(Student.number_of_students)
print('percentatge Student 1',objStudent_1.calculate_score_percentatge())
# usage of the calssmethod
Student.change_number_of_questions(95)
print('percentatge Student 1',objStudent_1.calculate_score_percentatge())
