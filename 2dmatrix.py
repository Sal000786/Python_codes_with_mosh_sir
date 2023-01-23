matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[1][0]=20
print(matrix[1][0])
matrix[0]=[10,20,30]
print(matrix,"new one")

for row in matrix:
    for item in row:
        print(item,end=" ")