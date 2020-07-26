print("------new line------")
a=5
b=9
# ternary operator
print("A") if a > b else print("=") if a == b else print("B")

if b > a:
      print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif a > b:
  print("a is greater than b")
else:
  pass
# Pass is required to put an empty condition block.x