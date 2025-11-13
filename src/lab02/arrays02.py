def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if len(nums)==0:
        raise ValueError
    return sorted(set(nums))
f=[1.0, 1, 2.5, 2.5, 0]
s=unique_sorted(f)
print(s)