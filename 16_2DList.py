# creating a  2D list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# accessing an element
print(matrix[0][2])

# printing the entire list
for row in matrix:
    for col in row:
        print(col)