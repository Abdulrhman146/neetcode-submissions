class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for array in matrix:
            new_array = set(array)
            if target in new_array:
                return True
            else:
                continue
        return False