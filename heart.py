# * *    * *
# *    *    *
#  *       *
#    *   *
#      *       

#heart

# Step 1: Loop through each row
for row in range(5):  # row goes 0,1,2,3,4
    # Step 2: Loop through each column
    for col in range(7):  # col goes 0,1,2,3,4,5,6
        # Step 3: Decide where to put stars
        if (row == 0 and (col == 1 or col == 2 or col == 4 or col == 5)) or \
           (row == 1 and (col == 0 or col == 3 or col == 6)) or \
           (row == 2 and (col == 0 or col == 6)) or \
           (row == 3 and (col == 1 or col == 5)) or \
           (row == 4 and col == 3):
            print("*", end="")  # print star and stay on same row
        else:
            print(" ", end="")  # print space and stay on same row
    print()  # move to the next row
