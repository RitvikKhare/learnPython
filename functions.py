def my_fun(fn, ln):
      print(fn + " " + ln)

my_fun("LO", "AD")

# when num of param is not known
def my_fun(*ln):
     for x in ln:
         print(x)

my_fun("gfh", "hhvj", "cykh")

# no order of parameterising
def my_fun(child3, child2, child1):
      print("The dump one is " + child3)

my_fun(child1 = "Ina", child2 = "Dika", child3 = "Mina")

# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
def my_fun(**selection):
      print("His last name is " + selection["lname"])

my_fun(fname = "Tobby", lname = "Roofus")


# default val of Parameter

def my_function(country = "India"):
      print("I am from " + country)
      country += " NoWay"
      return country

my_function("Sweden")
print(my_function())