def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError
    minimum = min(nums)
    maximum = max(nums)
    return (minimum, maximum)


f = [1.5, 2, 2.0, -3.1]
s = min_max(f)
print(s)
