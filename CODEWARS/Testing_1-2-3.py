"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples:

number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
"""

def number(lines):
    c = []
    for i in range(len(lines)):
        c.append(str(i+1) + ': ' + lines[i])
    return c


# oneliner with .enumerate
def number_1(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]


# oneliner with with .format and .xrange
def number(lines):
    return ["{0}: {1}".format(i + 1, lines[i]) for i in xrange(len(lines))]


# oneliner with .format and .xrange
def number(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]