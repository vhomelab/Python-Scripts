class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def printname(self):
        print(f"my name is {self.name}")


    def addage(self, age):
        self.age = self.age + age


p1 = person("vaseem", 41)
p1.printname()
p1.addage(2)

print(p1.age)