# mutable- means can add or remove, not indexed, don't allow duplicates,
# can't edit existing

thisset = {"ap", "ba", "ch","ap"}
print(thisset)

# needs to iterate only
for x in thisset:
  print(x)

newset = {'lm','mn'}

# + does not work have to use union
thisset=thisset.union(newset)
print(thisset)

newset = {'xy','yz'}

# update will insert item / set to existing
thisset.update(newset)
print(thisset)

# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets