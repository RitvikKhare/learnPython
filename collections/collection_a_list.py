# LIST ordered and changeable. Allows duplicate members

thislist = ["abc", "bcd", "cde", "def", "efg", "fgh", "ghi"]
#full list
print(thislist)

# 1st item
print(thislist[1])

# negative index ( second last )
print(thislist[-2])

# multiple indexes Range
print(thislist[2:5])

# single index range prints 2nd till end
print(thislist[2:])

# single index range prints from start till 5th
print(thislist[:5])

# length
print(len(thislist))

# it can be custom
customList = ["abc", 2 , "cde"]
print(customList)

# Iterating through list
for x in customList:
  print(x)

# search in list
if 2 in customList:
  print("Yes, 2 is in the custom list")

# Append in list
thislist.append("orange")
print(thislist)

# Change an element in list
thislist.insert(1, "DoubleOrgange")
print(thislist)

# Removing specific Item
thislist.remove("DoubleOrgange")
print(thislist)

# Removing last item when pop(<number is not given>)
thislist.pop()
print(thislist)

# poping with an index
thislist.pop(1)
print(thislist)

# clearing all items, emptying the list
thislist.clear()
print(thislist)

# deleting list
del thislist
# print(thislist) # will throw error as list has been deleted

# Copying a list in to another
customList.pop(1)
thislist = list(customList) # use customList.copy()
print (thislist , customList)

# concatinating list
thislist = thislist + customList
print(thislist)

# extends
thislist.extend(customList)
print(thislist)

# reverse
thislist.reverse()
print(thislist)

# sort
thislist.sort()
print(thislist)

# count
print(thislist.count('abc'))