class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        sa = sorted(list(set(heights)))
        max_v = max(sa)
        for i in range(len(sa)):
            stack = []
            for j, h in enumerate(heights):
              
                if h >= sa[i]:
                    stack.append(h)
                elif h < sa[i]:
                    stack = []
                max_v = max(max_v, len(stack)*sa[i])
        return max_v
