r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

matrix1 = []

for i in range(r1):
    row = list(map(int, input().split()))
    matrix1.append(row)

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

matrix2 = []

for i in range(r2):
    row = list(map(int, input().split()))
    matrix2.append(row)

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    result = [[0] * c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    print("Result:")
    for row in result:
        print(row)