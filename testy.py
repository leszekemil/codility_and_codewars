def solution(N):
    gap_list = [len(gap) for gap in bin(N)[2:].strip("0").split("1") if gap != ""]
    return max(gap_list) if gap_list else 0

print(solution(1041))