class Course(object):
    def __init__(self, name = 'Some Class', seats = 50):
        self.name = name
        self.seats = seats
        self.students = {}

    def isOpen(self):
        '''Return True if there are seats available in the course.'''
        return self.seats > len(self.students)

    def addStudent(self, Student):
        '''Add a student to the course.'''
        if self.isOpen():
            self.students[Student.name] = Student

            print 'There are %d seats left in %s' % \
                  (self.seats - len(self.students), self.name)
        else:
            print 'There are no seats left in this course - ' \
                    + 'the student cannot be added.'

    def removeStudent(self, Student):
        '''Remove a student from the course.'''
        try:
            del self.students[Student.name]

            print 'There are %d seats left in %s' % \
                  (self.seats - len(self.students), self.name)
        except:
            print 'That student is not enrolled in the class.'

    def __str__(self):
        s = 'There are %d students registered for %s \n' % \
               (len(self.students), self.name)

        for key, student in self.students.items():
            s = s + str(student) + '\n'

        return s