 #      * 
#     * * *
#    * * * *     
#   * * * * *    
#  * * * * * *   
# * * * * * * *
#       *
#       *
#       *
#       *

#christmas tree
# Define which columns have stars for each row
tree_rows = [
    [5],   # row 0
    [4, 5, 6],      # row 1
    [3, 4, 5, 6, 7],         # row 2
    [2, 3, 4, 5, 6, 7, 8],        # row 3
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [5],
    [5],
    [5],  
    [5]                                                                              # row 4
]

# Loop through each row
for row in range(len(tree_rows)):  # row = 0,1,2,3,4
    # Loop through each column (0 to 6)
    for col in range(11):
        if col in tree_rows[row]:  # check if this column should have a star
            print("*", end="")
        else:
            print(" ", end="")
    print()  # move to the next row