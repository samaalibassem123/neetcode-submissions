class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_arr = []
        for v in nums :
            if (v in temp_arr):
                return True
            temp_arr.append(v)
        return False
