class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        lettert = {}

        for i in s:
            if i in letters:
                letters[i] = letters[i] + 1
            else:
                letters[i] = 1
        for i in t:
            if i in lettert:
                lettert[i] = lettert[i] + 1
            else:
                lettert[i] = 1
        if len(letters) >= len(lettert):
            for k in letters.keys():
                if k in lettert:
                    if letters[k] == lettert[k]:
                        continue
                    else:
                        return False
                else:
                    return False
        else:  
            for k in lettert.keys():
                if k in letters:
                    if letters[k] == lettert[k]:
                        continue
                    else:
                        return False
                else:
                    return False
            
        return True

        