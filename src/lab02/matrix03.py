def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    f = len(mat[0])
    for z in mat:
        if len(z) != f:
            raise ValueError
    r = len(mat)
    k = len(mat[0])
    a = [0.0] * k
    for col in range(k):
        for row in range(r):
            a[col] += mat[row][col]

    return a


f = [[1, 2, 3], [4, 5, 6]]
l = col_sums(f)
print(l)
