

rows = 6
current_row = 0
total_width = 11

while current_row < rows:  # row = 0,1,2,3,4
    leading_spaces = current_row
    number_of_stars = total_width - (2 * current_row)
    print((" " * leading_spaces) + ("*" * number_of_stars))
    current_row +=1
    

# inverted triangle //original logic
# length=5
# row = 1
# while row <= length:
#     if row == 1:
#      print("*" * length) 
#     else: print ((" " *(length-1) )+("*" * length))
#     length-= 1





