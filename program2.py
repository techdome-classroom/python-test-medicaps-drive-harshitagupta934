class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        
        prev_value = 0
        for char in reversed(s):
            curr_value = roman_dict[char]
            if curr_value < prev_value:
                result -= curr_value
            else:
                result += curr_value
            prev_value = curr_value
        
        return result

# Test cases
solution = Solution()
print(solution.romanToInt("III"))     
print(solution.romanToInt("LVIII"))   
print(solution.romanToInt("MCMXCIV")) 
