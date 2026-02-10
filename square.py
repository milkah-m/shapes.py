# hollow square
length = 5
# row = ("*" * 4)
row = 1
while row <= length:
   if row == 1 or row == length:
     print("*" * length)
   else: 
      print("*" + " " * (length-2) + "*")
   row += 1
