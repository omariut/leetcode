"""
Runtime: 27 ms, faster than 96.00% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.9 MB, less than 73.93% of Python3 online submissions for Valid Parentheses.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if s[-1] == '(' or s[-1] == '{' or s[-1] == '[':
            return False

        x = []

        for index, item in enumerate(s):

            if item == '(' or item == '{' or item == '[':
                x.append(item)

            if x == []:
                return False

            else:

                if item == ')':

                    if x[-1] == '(':
                        del x[-1]
                    else:
                        return False

                if item == '}':
                    if x[-1] == '{':
                        del x[-1]
                    else:
                        return False
                if item == ']':
                    if x[-1] == '[':
                        del x[-1]
                    else:
                        return False

        if x == []:
            return True

        return False


s = "(])"
x = Solution()
x = x.isValid(s)
print(x)
