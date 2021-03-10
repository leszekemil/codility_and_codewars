"""
Complete the function scramble(str1, str2) that returns true if a portion of str1
characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""

from collections import Counter

def scramble(s1, s2):
    letters = Counter(s1)
    word = Counter(s2)
    diff = word - letters
    return len(diff) == 0

# def scramble(s1, s2):
#     a = list(s1)
#     b = list(s2)
#     n = 0
#     while True:
#         try:
#             if b[n] in a:
#                 a.remove(b[n])
#                 n += 1
#             else:
#                 return False
#         except IndexError:
#             return True

# def scramble(s1, s2):
#     if (set(s1) & set(s2)) == set(s2):
#         return True
#     else:
#         return False