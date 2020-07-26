class MyClass:
  x = 5

class PersonClass:
    def __init__(self, nameProp, ageProp):
        self.nameProp = nameProp
        self.ageProp = ageProp

    def classfunc(self):
        print("Function Prop Value Name = " + self.nameProp)

    def printdetail(self):
        return [self.nameProp, self.ageProp]

class Student(PersonClass):
      def __init__(self, fname, lname,studentID):
        #add properties etc
        PersonClass.__init__(self,fname,lname)
        # can be written as super().__init__(self,fname,lname):
        self.studentId = studentID

      def newFunctionAdded(self):
          print ("New function added to the class")

class EmptyClass:
    pass

# Inherit Class
class Employee(PersonClass):
  pass

# object declaration  
p1 = MyClass()
print('Value from object =',p1.x)

p1 = PersonClass("Sunny", 33)
print("Name =",p1.nameProp)
print("Age =",p1.ageProp)

# calling funciton
p1.classfunc()

print ("Value of object",p1)
p1.ageProp = 40

print ("Age prop updated = ",p1.ageProp)

# del p1.ageProp
# del p1 

obj2 = Employee("InheritClass", 50)
print("Name = ", obj2.ageProp , "GDF = ", obj2.nameProp)

obj3 = Student("Pappu", 20 , "PA9798")
print ("Student detail = ",obj3.printdetail(),obj3.studentId)
obj3.newFunctionAdded()