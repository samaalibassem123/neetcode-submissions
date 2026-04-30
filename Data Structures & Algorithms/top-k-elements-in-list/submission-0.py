class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = defaultdict(int)
        for i , value in enumerate(nums):
            num_to_freq[value] += 1
            

        sorted_by_freq = sorted(num_to_freq.items(), key=lambda x:x[1], reverse=True)
        res = [val for val , _ in sorted_by_freq[:k]]
        return res

        