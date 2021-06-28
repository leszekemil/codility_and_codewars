'https://stackoverflow.com/questions/6076270/lambda-function-in-list-comprehensions'
# Why is the output of the following two list comprehensions different, even though f and the lambda function are the same?
f = lambda x: x*x
[f(x) for x in range(10)]
# and
[lambda x: x*x for x in range(10)]
# Mind you, both type(f) and type(lambda x: x*x) return the same type.

# The first one creates a single lambda function and calls it ten times.
# The second one doesn't call the function. It creates 10 different lambda functions. It puts all of those in a list. To make it equivalent to the first you need:
[(lambda x: x*x)(x) for x in range(10)]
# Or better yet:
[x*x for x in range(10)]


"""
Using a list comprehension, create a new list called "newlist" out of the list "numbers", which contains
only the positive numbers from the list, as integers.
"""
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [i for i in numbers if i >= 0]
print(newlist)

"""
Create an identical list from the first list using list comprehension.
"""

lst1=[1,2,3,4,5]

lst2=[i for i in lst1]
lst2=[i for i in range(1,6)]

print(lst2)

"""
Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
"""

lst=[i for i in range(1200,2000,130)]


"""Words not 'the'
Given a sentence, produce a list of the lengths of each word in the sentence, but only if the word is not 'the'.
    >>> words_not_the('the quick brown fox jumps over the lazy dog')
    [5, 5, 3, 5, 4, 4, 3]
"""
sent = 'the quick brown fox jumps over the lazy dog'

b = [len(i) for i in sent.split() if i!='the']

"""Vowels:
Given a string representing a word, write a list comprehension that produces a list of all the vowels in that word.
    >>> vowels('mathematics')
    ['a', 'e', 'a', 'i']
"""

b = [i for i in sent if i in ('a','o','e','i','u')]

"""Vowels set:
Given a string representing a word, write a set comprehension that produces a set of all the vowels in that word.
    >>> vowels_set('mathematics')
    set(['a', 'i', 'e'])
"""

b = {i for i in sent if i in ('a','o','e','i','u')}

"""Disemvowel:
Given a sentence, return the sentence with all vowels removed.
    >>> disemvowel('the quick brown fox jumps over the lazy dog')
    'th qck brwn fx jmps vr th lzy dg'
"""

b = [i for i in sent if i not in ('a','o','e','i','u')]
print(''.join(b))

b = ''.join([i for i in sent if i not in ('a','o','e','i','u')])


"""Wiggle numbers:
Given a list of number, return the list with all even numbers doubled, and all odd numbers turned negative.
    >>> wiggle_numbers([72, 26, 79, 70, 20, 68, 43, -71, 71, -2])
    [144, 52, -79, 140, 40, 136, -43, 71, -71, -4]
"""

b = [i*2 if i%2==0 else abs(i)*-1 if i%2!=0 else i for i in sent]

"""Encrypt lol:
Given a sentence, return the setence will all it's letter transposed by 1 in the alphabet, but only if the letter is a-y.
    >>> encrypt_lol('the quick brown fox jumps over the lazy dog')
    'uif rvjdl cspxo gpy kvnqt pwfs uif mbzy eph'
"""

a = [chr(ord(i) + 1) if i != ' ' and i < 'y' else i for i in sent]

'''
Find all of the numbers from 1-1000 that have a 3 in them
'''

three = [n for n in range(0,1000) if '3' in str(n)]


'''
Given numbers = range(20), produce a list containing the word 'even' if a number in the numbers is even, and the word
'odd' if the number is odd.  Result would look like ['odd','odd', 'even']
'''

result = ['even' if n%2 == 0 else 'odd' for n in range(20)]
b = ['ood' if i%2==0 else 'even' if i%2!=0 else i for i in sent]

'''
Produce a list of tuples consisting of only the matching numbers in these lists list_a = [1, 2, 3,4,5,6,7,8,9], list_b = [2, 7, 1, 12].  Result would look like (4,4), (12,12)
'''

result = [(a,b) for a in list_a for b in list_b if a==b]

'''
Find the common numbers in two lists (without using a tuple or set) list_a = [1, 2, 3, 4], list_b = [2, 3, 4, 5]
'''

result = [i for i in list_a if i in list_b]

"""
For each number in list_b, get the number and its position in mylist as a list of tuples.
"""

g = [(i,mylist.index(i)) for i in list_b]

"""
thise same but dict
"""

g = {i : mylist.index(i) for i in list_b}