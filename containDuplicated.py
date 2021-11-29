class Solution:
    def containsDuplicate(self, nums) -> bool:

        # for i in range (0, len(nums)):
        #    for j in range (0, i):
        #       if nums[i] == nums[j]:
        #          return True
        # return False
        nums.sort()
        for i in range(0, len(nums) - 1):
            if (nums[i] == nums[i + 1]):
                return True
        return False


