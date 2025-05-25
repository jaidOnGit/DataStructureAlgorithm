class AddBinary:
    def __str__(self):
        return """
        67. Add Binary
        Given two binary strings a and b, return their sum as a binary string.
        """
    
    def addBinary(self, a: str, b: str) -> str:
        integer_to_binary = lambda integer : "{0:b}".format(integer)
        return integer_to_binary(int(a, 2) + int(b, 2))
    
class MergeStringsAlternately:
    def __str__(self):
        return """
        1768. Merge Strings Alternately
        You are given two strings word1 and word2. 
        Merge the strings by adding letters in alternating order, starting with word1. 
        \If a string is longer than the other, append the additional letters onto the end of the merged string.
        Return the merged string.
        """
    
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedstr = str()        
        n = len(word1) + len(word2)
        while n > 0:
            if len(word1) > 0:
                mergedstr += word1[0]
                word1 = word1[1:]
                n -= 1
            if len(word2) > 0:
                mergedstr += word2[0]
                word2 = word2[1:]
                n -= 1
        return mergedstr

class FindFirstOccurrance:
    def __str__(self):
        return """
        28. Find the Index of the First Occurrence in a String
        Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
        """
    
    def strStr(self, haystack: str, needle: str) -> int:
        # pythonista
        index = -1
        if needle in haystack:
            index = haystack.index(needle)
        return index
    
    # Rabin-Karp algorithm
    