# dostajesz ciąg int
# zwraca indice dwóch numb ktore dodają się w okreslony target. Zakładasz, że kązdy input ma 1 rozw,
# i nie uzywasz tego samego dwa razy.

inp = [2,7,11,15]
target = 9

#1 Podwójna pętla for
def solution(inp,target):
    for i in range(len(inp)):
        for j in range(i+1, len(inp)):
            if inp[i] + inp[j] == target:
                return([i,j], inp[i] , inp[j])

print(solution(inp,target))
# ([0, 1], 2, 7)

#2 Z uzyciem słownika przechowującego dane
def solution2(inp,targrt):
    seen = {}
    for index, num in enumerate(inp):
        if target - num in seen:
            return([seen[target-num], index])
        elif num not in seen:
            seen[num] = index

print(solution2(inp,target))
# [0, 1]