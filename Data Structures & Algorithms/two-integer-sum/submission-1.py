class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap  = {i:val for val , i in enumerate(nums)}
        for i , val in enumerate(nums):
            n = target - val
            if(n in nums and hashmap[n] != i):
                return [i, hashmap[n]]