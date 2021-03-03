"""
Mamy schody z N stopniami.
Można się wspinać 1 lub 2 stopnie na raz.
Napisz funkcje która zwraca unikalne sposoby wejścia na schody. Kolejniśc schodów ma znaczenie.
For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
"""

def solution(N):
    a,b = 1,2
    solu = []
    for i in range(N-1):
        a,b = b, a+b
        solu.append(a)
    return a,solu

print(solution(4))


def sol2(N):
    a,b = 1,2
    if N<=1:
        return 1
    return sol2(N-1)+sol2(N-2)

print(sol2(4))

def open_or_senior(data):
    out = []
    for i in data:
        if i[0] >= 50:
            return "Senior"
        else:
            return "Open"



print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
