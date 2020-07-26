astr = '''Line 1 : multiple line string 
Line 2 : providing spaces and new lines in between
Line 3 : to check if it is printed in new line'''
print(astr)

# string as array 
a = "    Udayam, Hyderabad!    "
print('String as = ' + a)
print('Array Element at 10 = ' + a[10])
# slice 
print('Slice from 12 : 15 = ' + a[12:15])

# negative indexing
print('Negative indexing -10: -6 = ' + a[-10:-6])

# length returns a number
print('Length of string = ' + str(len(a)))

# trim - remove spaces from string 
print('Removing spaces = ' + a.strip())

# all lower
print('all lower = ' + a.lower())
# all upper
print('all upper = ' + a.upper())

# replace 
print('Replace H with J = ' + a.replace("H", "J"))

# split returns a list, can not concatenate with string directly
print('Split by , = ' + str(a.split(',')))
print('Can be directly printed as = ')
print(a.split(','))

# Search in String returns true/false boolean
txt = "The fun in Rain is temporary"
x = "ain" in txt
y = 'notpreset' in txt
print ('String to be searched in = ' + txt)
print ('String to be searched = ain' )
print('Present = '+ str(x))
print ('String to be searched = notpresent')
print ('Not Present ' + str(y))

# Passing Values
quant = 3
item = 567
price = 49.95
print ('Values quant = ' + str(quant) + ' | item = ' + str(item) + ' | price = ' + str(price))
myorder = "third {2} first {0} second {1}."
print ('Ordering ' + myorder + '\nValues = ' + myorder.format(quant, item, price))
myorder = "third {} first {} second {}."
print('No Ordering '+ myorder + '\nValues = ' + myorder.format(quant, item, price))
# Partial Ordering Gives Error
# myorder = "third {2} first {} second {}."
# print('Partial Ordering '+ myorder + '\nValues = ' + myorder.format(quant, item, price))

# Same Ordering Gives Error
myorder = "third {2} first {2} second {2}."
print('Same Ordering '+ myorder + '\nValues = ' + myorder.format(quant, item, price))

# Hexa Value \xhh , Octal Values \ooo
txt = "\x48\x65\x6c\x6c\x6f"
print('Hexa value ' + txt) 
txt = "\110\145\154\154\157"
print('Octal Value '+ txt)

