class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:\
        # search on wich row the target exist 
        lR, rR = 0 , len(matrix) -1
        
        while lR <= rR:
            global m
            m = lR + ((rR - lR) // 2)
            if target < matrix[m][0] and target < matrix[m][-1]  :
                rR = m - 1
            elif target > matrix[m][0] and target > matrix[m][-1]:
                lR = m + 1
            else :
                break
        if lR > rR:
            return False
        
        # seach on columns
        lc , rc = 0, len(matrix[m]) - 1

        while lc <= rc : 
            mc = lc + ((rc - lc) // 2)

            if matrix[m][mc] < target:
                lc = mc + 1
            elif matrix[m][mc] > target:
                rc = mc - 1
            else :
                return True

        return False 

        
            