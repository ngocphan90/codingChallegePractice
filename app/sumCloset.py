# Given an integer array nums of length n and
# an integer target, find three integers in nums such
# that the sum is closest to target.
# Return the sum of the three integers (leetcode problem)
def threeSumClosest(nums, target):
    diff = float('inf')
    nums.sort()
    print(nums)
    for i in range(len(nums)):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if abs(target - sum) < abs(diff):
                diff = target - sum
            if sum < target:
                lo += 1
            else:
                hi -= 1
        if diff == 0:
            break
    return target - diff


print(threeSumClosest([-1, 2, 1, -4], 1))