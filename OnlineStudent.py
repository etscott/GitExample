from Student import *

class OnlineStudent(Student):
    def __init__(self, name, age, major, location):
        super(OnlineStudent,self).__init__(name, age, major)
        self.location = location

    def __str__(self):
        return '%s,\t\t%d,\t\t%s, \t\t%s' % \
               (self.name, self.age, self.major, self.location)
