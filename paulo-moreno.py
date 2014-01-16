class student:
    courseMarks={}

    def __init__(self,courseName):
        self.courseName = courseName
        self.courseMarks = {}

    def addCourse(self, course, mark):
    	self.courseMarks[course] = mark

    def average(self):
    	sum = 0
        for key in self.courseMarks:
        	sum += self.courseMarks[key]
        return sum/len(self.courseMarks)