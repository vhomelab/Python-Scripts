class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f'{self.firstname} {self.lastname}')


class Student(Person):
    def __init__(self, fname, lname, gradyear):
        super().__init__(fname, lname)

        self.graduationyear = gradyear

    def printdetails(self):
        print(f'{self.firstname} {self.lastname} graduated in the year {self.graduationyear}')

    def changeyear(self, gradyear):
        self.graduationyear = gradyear


student1 = Student("vaseem", "mohammed", 2005)

student1.printname()
student1.printdetails()

student1.changeyear(2006)

student1.printdetails()
