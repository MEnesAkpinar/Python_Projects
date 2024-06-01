"""
Given an integer x, return true if x is a palindrome, and false otherwise.

"""

def isPalindrome(x):
        a = str(x)
        return a == a[::-1]