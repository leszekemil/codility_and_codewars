"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace
at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""
string = "apples, pears # and bananas\ngrapes\nbananas !apples"
markers = ["#", "!"]

#1
def solution2(string,markers):
    s = string.split("\n")
    result = ""
    for i in s:
        trimmed = ""
        for j in i:
            if j not in markers:
                trimmed += j
            else:
                break
        trimmed = trimmed.rstrip()
        result = result + trimmed + "\n"
    return result[:-1]


print(solution2(string,markers))


#2
def solution3(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)