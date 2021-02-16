"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded
by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1.
The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and
has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its
longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary
representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""

# 1
def solution(N):
    bnr = str(bin(N))[2:]
    max = 0
    accumu = 0

    for i in bnr:
        if i == '0':
            accumu += 1

        elif i == '1':
            if accumu > max:
                max = accumu
            accumu = 0

    return max

print(solution(1041))


# 2
def solution2(N):
    cnt = 0
    result = 0
    found_one = False

    i = N

    while i:
        if i & 1 == 1:
            if (found_one is False):
                found_one = True
            else:
                result = max(result, cnt)
            cnt = 0
        else:
            cnt += 1
        i >>= 1

    return result

print(solution2(1041))


# 3
def countBinaryGap(num):
    binary = format(num , "b")
    print("Longest Binary Gap in :" + binary)
    gap = False         # to indicate if there is a gap
    counter = 0         # to count zeros in each gap
    last = ''           # to store last iteration value
    binary_gap = 0      # to store longest gap value
    for s in binary:
        if last == '':
            last = str(s)
            continue
        else :
            if s == '0':
                if last == '1':
                    counter += 1
                    last = '0'
                    gap = True
                    continue
                if last == '0':
                    if counter > 0 :
                        counter += 1
                        last = '0'
                        continue
                    if counter == 0:
                        last = '0'
                        continue
            if s == '1':
                if gap == True :
                    if last == '0':
                        if counter > binary_gap:
                            binary_gap = counter
                        counter = 0
                        last = '1'
                        gap == False
                        continue
                if gap == False:
                    if last == '0':
                        last = '1'
                        continue
                    if last == '1':
                        last = '1'
                        continue
    return binary_gap