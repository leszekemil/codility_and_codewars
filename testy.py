string = "abba"

def solution(string):
    g = string.split()
    d = "".join(g).lower()
    l = []
    for i in d:
        l.append(i)
    for j in l:
        if l.count(j) == 1:
            return j


def first_non_repeating_letter(string):
    lowercase=string.lower()
    for i,letter in enumerate(lowercase):
        if lowercase.count(letter)==1:
            return string[i]
    return ''


def first_non_repeating_letter(string):
    low_str = []
    for i in string:
        low_str.append(i.lower())
    for i in string:
        if low_str.count(i.lower()) == 1:
            return i
    return ''
