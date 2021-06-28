"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation
marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

#1 ONELINER
def pig_it(text):
    return ' '.join([x[1:]+x[0]+"ay" if x not in ['!','.','?'] else x for x in text.split()])


#2
def pig_it(text):
    words = text.split(" ")

    new_words = []

    for word in words:
        if word.isalpha():
            new_word = word[1:] + word[0] + "ay"
            new_words.append(new_word)
        else:
            new_words.append(word)
    return " ".join(new_words)

#3
def pig_it(text):
    t2 = text.split()
    t3 = []
    for i in t2:
        j = i[1:] + i[0] + "ay"
        t3.append(j)
    return ' '.join(t3)