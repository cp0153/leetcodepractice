def solution(A, X):
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l < r:
        m = (l + r) // 2
        if A[m] > X:
            r = m - 1
        else:
            l += 1
    if A[l] == X:
        return l
    return -1


print(solution([1, 2, 5, 9, 9], 5))
print(solution([1, 2, 3, 4], 5))
print(solution([1, 2, 3, 4, 4, 7, 8, 11], 11))
print(solution([-11, -2, 3, 4, 4, 7, 8, 11], -3))
print(solution([-11, -2, 3, 4, 4, 7, 8, 11], 3))
print(solution([-11, -2, 3, 4, 4, 7, 8, 11], -11))
