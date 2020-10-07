# Mitch Rogers
# Objects within Objects, Objects as Lists

from datetime import datetime

class Student :
    universityName = "CP University"
    nextID = 1

    def __init__(self, fName, lName) :
        self.studentID = Student.nextID
        Student.nextID += 1
        self.firstName = fName
        self.lastName = lName
        self.course = None
        self.totalCredits = 0

    def getInfo(self) :
        return ("Student " + str(self.studentID) + " " + self.firstName + " " + self.lastName +
                " total credits are " + str(self.totalCredits)) 

class Course :

    def __init__(self, num, title, credit, studentOwner) :
        self.courseNum = num
        self.courseTitle = title
        self.courseCredits = credit
        self.passedCourse = False
        self.finalExam = FinalExam(self, studentOwner)

class FinalExam :
    
    def __init__(self, courseOwner, studentOwner) :
        self.testDatetime = None
        self.testLocation = ""
        self.testScore = 0
        self.courseOwner = courseOwner
        self.studentOwner = studentOwner

    def setTest(self, datetime, loc, score) :
        self.testDatetime = datetime
        self.testLocation = loc
        #self.courseOwner.passedCourse = self.passCourse(score)

    def passCourse(self, score) :
        self.testScore = score

