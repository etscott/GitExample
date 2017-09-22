class Student(object):
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return '%s,\t\t%d,\t\t%s' % \
               (self.name, self.age, self.major)
