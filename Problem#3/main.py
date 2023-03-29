class Solution(object):
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        if s:
            output = s[0]
        else: return 0
        max_counter = 0
        for i in s:

            if i not in output:
                output += i
                counter += 1
            else:
                counter = 0
                output = []
            if counter > max_counter:
                max_counter = counter
        return max_counter


s = "aab"

print(f"{Solution.lengthOfLongestSubstring(s)}")