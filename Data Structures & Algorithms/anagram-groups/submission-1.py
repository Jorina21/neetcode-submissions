class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import string

        #createt a-z
        alphabet = string.ascii_lowercase

        print(alphabet)

        my_dict = {} #dict literal 

        for word in strs:

            #word --> number @ aphabet 
            

            my_tuple = tuple(word.count(char) for char in alphabet) #expression for item in iteratble 
        
            # print(my_tuple)

            #add tuple as key 
            if my_tuple not in my_dict:
                my_dict[my_tuple] = [word]

            else: 
                my_dict[my_tuple].append(word)

        
        anagrams = []

        for values in my_dict.values():

            anagrams.append(values)

        # print(anagrams)
        return anagrams
        
