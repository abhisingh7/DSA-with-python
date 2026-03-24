# prefix sum

def build_prefix(nums):
    prefix = [0]
    
    # with range loop
    # for i in range(len(nums)):
    #     prefix.append(prefix[i]+nums[i])
    
    # without range loop
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix 


def range_sum(nums, prefix, left, right):
    if right >= len(nums) or left < 0:
        return -1  # or raise an exception
    return prefix[right + 1] - prefix[left]

    
nums   = [3, 1, 4,  1,  5,  9,  2,  6]
prefix = build_prefix(nums)
print(prefix)

left = 2
right = 5
print(range_sum(nums, prefix, left, right))