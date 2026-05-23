class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = ''.join(c for c in s if c.isalnum())
        new_s = new_s.lower()

        length = len(new_s) // 2
        
        for idx, i in enumerate(new_s):
            right_side = -idx - 1
            if new_s[idx] == new_s[right_side]:
                continue
            else:
                return False
        return True