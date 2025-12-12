def transpose(mat):
    if not mat:
        return []
    row_length = len(mat[0])
    for p in mat:
        if len(p) != row_length:
            raise ValueError
    r = []
    for i in range(len(mat[0])):
        g = []
        for p in mat:
            g.append(p[i])
        r.append(g)
    return r


print(transpose([[1, 2], [3, 4]]))
