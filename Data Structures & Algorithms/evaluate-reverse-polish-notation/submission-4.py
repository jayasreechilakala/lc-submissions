class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i in {"+", "-", "*", "/"} and stk and len(stk) >= 2:
                a, b = stk.pop(), stk.pop()
                if i == "+":
                    stk.append(a + b)
                elif i == "-":
                    stk.append(b - a)
                elif i == "*":
                    stk.append(a * b)
                elif i == "/":
                    stk.append(int(b / a))
            else:
                stk.append(int(i))
        print(stk)
        return (stk[-1])