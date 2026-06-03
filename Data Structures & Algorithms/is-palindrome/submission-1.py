class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = '' #create an empty string

        for c in s:
            if c.isalnum(): #check if c is alphanumeric a-z, 0-9
                newStr += c.lower() #adding all letters and/or numbers to the newStr
        return newStr == newStr[::-1] #returns true if string is the same forward and reverse

        

