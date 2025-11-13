def row_sums(mat: list[list[float | int]]) -> list[float]:
    result = []
    for i in mat:
        if len(i)<=1:
            raise TypeError
        i = sum(i)
        result.append(float(i))
    return result
s= [
    [1,2,3],
    [4,5,6]
]
f=row_sums(s)
print(f)
