nums = [1, 2, 3, 4]

def containsDuplicate(nums: list[int]) -> bool:
    if nums == list(set(nums)):
        return False
    else:
        return True

print(nums)
print(list(set(nums)))
print(containsDuplicate(nums=nums))

#Input: nums = [1, 2, 3, 1]
#Output: true

#Input: nums = [1, 2, 3, 4]
#Output: false
