class Solution:
    def rotate(self, nums, k) :
        k %= len(nums)
        l = len(nums)
        # for i in range (k):
        #    previous = nums[l-1]
        #   for j in range (l):
        #      temp = nums[j]
        #     nums[j] = previous
        #    previous = temp

        # nums[k:], nums[:k] = nums[:-k], nums[-k:]
        print(nums[k:])
        print(nums[:-k])
        print(nums[:k])
        print(nums[-k:])