"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.


"""


def lengthOfLastWord(s):

    liste = []

    liste = s.split()


    return len(liste[-1])

    a = s.split()[-1]

    b = len(s.split()[-1])


s = "   fly me   to   the moon  " 




print(lengthOfLastWord(s))

