class Solution:
    def isPalindrome(self, s: str) -> bool:
        #covert to lower case 
        
        #re.sub(pattern, replacement, string)
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        print(s)
        

        left = 0
        right = len(s)-1 

        while left <= right:


            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                return False

        return True


        