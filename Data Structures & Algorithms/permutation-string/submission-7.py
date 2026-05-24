class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_len = len(s1)
        s2_len = len(s2)

        left = 0
        right = s1_len

        while right <= s2_len:
            if sorted(s2[left:right]) == sorted(s1):
                return True
            right += 1
            left += 1
        return False # finish

        