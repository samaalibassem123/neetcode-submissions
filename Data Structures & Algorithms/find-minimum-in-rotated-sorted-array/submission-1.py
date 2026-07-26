class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums)-1
        res = nums[0]
        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            m = l + ( (r - l) // 2 )

            res = min(res, nums[m])

            if nums[m] < nums[r]:
                r = m - 1
            elif nums[m] >= nums[l]:
                l = m + 1
        
        return res