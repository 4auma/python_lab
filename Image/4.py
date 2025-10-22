def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
#Проверка на пустой список:
    if len(nums)==0:
        raise ValueError
    minimum=min(nums)
    maximum=max(nums)
    return (minimum,maximum)
f=[1,2,3,4,5,6]
s=min_max(f)
print(s)