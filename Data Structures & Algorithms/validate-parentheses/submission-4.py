class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        n = len(s)
        if not s or n % 2 != 0:
            return False
        closed = {"]": "[", ")": "(", "}": "{"}
        i = 0
        while i < n:
            if s[i] not in closed:
                stk.append(s[i])
                i += 1
            elif (stk and stk[-1] == closed[s[i]]):
                    stk.pop()
                    i += 1
            else:
                return False
        return True if not stk else False


        
