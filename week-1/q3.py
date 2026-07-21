def multiply(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A)):
            sum = 0
            for k in range(len(A)):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)

    return result
def power(A, m):
    result = A
    for i in range(m - 1):
        result = multiply(result, A)
    return result
def main():
    A = [[1, 2],
         [3, 4]]
    m = 3
    ans = power(A, m)
    print("A^", m, "is:")
    for row in ans:
        print(row)
main()