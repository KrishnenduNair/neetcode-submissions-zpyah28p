class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        low, hi = 0, m*n-1

        while low <= hi:
            mid = (low+hi) // 2
            row, col = mid//n, mid%n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                low = mid + 1
            elif val > target:
                hi = mid-1

        return False

            


        
    

                

                
            