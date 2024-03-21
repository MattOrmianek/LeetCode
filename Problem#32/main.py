# This was one of good solutions
#class Solution(object):
#    def longestValidParentheses(self, s):
#        """
#        :type s: str
#        :rtype: int
#        """
#        stack = []
#        l = ['0'] * len(s)
#        for index, element in enumerate(s):
#            if element == '(':
#                stack.append(index)
#            else:
#                if stack:
#                    l[stack.pop()] = '1'
#                    l[index] = '1'

#        return max(len(i) for i in ''.join(l).split('0'))


# Yet that was my first solution
# TODO: still needs to be fixed
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = []
        is_open = False
        validated_parentheses = 0
        for i in range(len(s)):
            element = s[i]
            if element == "(":
                if is_open or not temp:
                    temp.append(element)
                is_open = True
            else:
                if temp and not is_open:
                    temp.pop()
                if temp:
                    validated_parentheses = max(validated_parentheses, i - temp[-1] + 1)
                is_open = False

        return validated_parentheses
