def flat(mat: list[list | tuple]) -> list:
    result = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            raise TypeError
        for g in i:
            if isinstance(g, (list, tuple)):
                raise TypeError
            result.append(g)
    return result


s = [[1], [], [2, 3]]
s = flat(s)
print(s)
