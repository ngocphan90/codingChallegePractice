def maxSubArray(nums):
    #initialize first element into our current and max sub array
    current_sub = max_sub = nums[0]
    for num in nums[1:]:
        current_sub = max(num, current_sub+num)
        max_sub = max(current_sub, max_sub)
    return max_sub

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))