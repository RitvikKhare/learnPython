# unordered, changeable and indexed. 
# keys and values.
# basically Json format : 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "object" : {
      "abc" : "ijoida123"
  }
}
print(thisdict)

thisdict["object"] = "avalue assignment"
print(thisdict)

# loop through
for x in thisdict:
    print("Key = " + x)
    print("Value =" , thisdict[x])

# printing only values
for x in thisdict.values():
    print(x)

# key and value exists
for x , y in thisdict.items():
    print (x , y)

# check if value exists
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# length
print("Length =" , len(thisdict))

# Add a key 
thisdict["color"] = "red"
print("Added Key =",thisdict)

# Delete specific Key
thisdict.pop("model")

# Delete popitem
thisdict.popitem()

print("Deleting model, last item ",thisdict)

# deletes a specific key
# del thisdict["model"]
# del thisdict
# thisdict.clear()

print("clear dictionary=", thisdict)

# Copy
newdict = thisdict.copy()

print("copied", newdict)

# New dictionary 
dictionaryCollection = {
    "diction1" : thisdict,
    "diction2" : newdict
}

print("dictionaryCollection",dictionaryCollection)