"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
"""

# 1
def namelist(names):
    stri = ""
    l = []
    if len(names) != 1:
        for i in range(len(names) - 1):
            l.append(names[i]['name'])
        stri = ', '.join(l)
        stri += ' & ' + names[-1]['name']
        return stri
    else:
        return names[i]['name']


# 2 dobrze zrobione
def namelist(names):
    str = ''
    if len(names) != 0:
        arr = []
        for i in range(0, len(names) - 1):
            arr.append(names[i]['name'])
        str = ', '.join(arr)
        str += ' & ' + names[-1]['name'] if str != '' else names[-1]['name']

    return str


# 3 ładnie
def namelist(names):
    if len(names) == 0: return ''
    if len(names) == 1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']