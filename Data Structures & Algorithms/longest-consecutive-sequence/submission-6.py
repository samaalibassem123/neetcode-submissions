class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums =  list(sorted(set(nums)))
        if len(nums) == 0:
            return 0
        max_c = 1
        res = 1
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] + 1 ==  nums[i+1] :
                res = res + 1
            else :
                max_c = max(res, max_c)
                res = 1
            max_c = max(res, max_c)
            print(res, max_c)
        return max_c