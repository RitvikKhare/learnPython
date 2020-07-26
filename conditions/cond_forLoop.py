# we already know the "for x in list/dict/sets/tuples"

# range

for x in range(2):
    print (x)

for x in range(7,9):
    print(x)
 
# Empty loop
for x in [0, 1, 2]:
  pass

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#error trial
for x in adj:
    for x in fruits:
      print(x,x)

for x in range(2):
    for x in range(3):
        print(x)