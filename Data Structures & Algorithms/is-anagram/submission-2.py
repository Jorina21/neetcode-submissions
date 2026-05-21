class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #dictornary key being the letters value being how the frequency

        #mew_dict = {key_expression: value_expression for item in iterable}
        s_dict = {word : s.count(word)  for word in s} #frequency counter via dictionary comprehension

        print(s_dict)

        for char in t:
            if char not in s_dict:
                return False
            
            s_dict[char] -= 1
        
        return all(val == 0 for val in s_dict.values())