# Most values are true
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(["", "", ""]))
# False Values 
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# False Object class obj that returns 0 from __len__ function for self
class myclass():
      def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

# true object
class myclass():
      def __len_(self):
        return 0
myobj = myclass()
print(bool(myobj))

def myFunction() :
      return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# function returning boolean value
x = 200
print(isinstance(x, int))