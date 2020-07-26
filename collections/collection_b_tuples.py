# all functions applied similar to list except value changes or size change.
# IMMUTABLE 

x = ("ap", "ba", "ch")
y = list(x)
y[1] = "ki"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")

# clubbing tuple is possible.
thistuple = thistuple + x

print(thistuple)
# deleting tuple is possible.
del thistuple
