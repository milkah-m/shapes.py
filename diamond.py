
#       * 
#     * * *
#    * * * *     
#   * * * * *    
#  * * * * * *   
# * * * * * * *
#  * * * * * *  
#   * * * * *   
#    * * * *   
#     * * *   
#       * 
#diamond
diamond_rows = [
    [5],   # row 0
    [4, 5, 6],      # row 1
    [3, 4, 5, 6, 7],         # row 2
    [2, 3, 4, 5, 6, 7, 8],        # row 3
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 4, 5, 6, 7, 8], 
    [3, 4, 5, 6, 7],
    [4, 5, 6],
    [5], 
]

for row in range(len(diamond_rows)):  # row = 0,1,2,3,4
    # Loop through each column (0 to 6)
    for col in range(11):
        if col in diamond_rows[row]:  # check if this column should have a star
            print("*", end="")
        else:
            print(" ", end="")
    print()