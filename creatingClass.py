class StudentInfo(object):
    def __init__(self,name,rollNo,grade,marks):
        self.name = name
        self.rollNo = rollNo
        self.grade = grade
        self.marks = marks
    
    def evaluate(self):
    
        if(self.marks > 90):
            print('EXCELLENT!')

        elif(89 > self.marks > 50):
            print('GOOD!')

        elif(49 > self.marks > 30):
            print('NEEDS IMPROVEMENT')

        elif(self.marks < 30):
            print('HARD WORK STUDENT')

Vatsal = StudentInfo('Vatsal Varenya',35,9,29)

Vatsal.evaluate()