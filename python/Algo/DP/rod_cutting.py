from typing import List

def rod_cutting_recurr(n: int, value: List[int]):
    if n == 0:
        return 0
    q = float("-inf")
    for i in range(1, n+1):
        q = max(q, value[i-1]+rod_cutting_recurr(n-i, value))
    return q

def rod_cutting_recurr_old(n: int, value: List[int]):
    if n == 0:
        return 0
    q = value[n-1]
    for i in range(1, n+1):
        q = max(q, rod_cutting_recurr(i, value)+rod_cutting_recurr(n-i, value))
    return q

def rod_cutting(n: int, value: List[int]):
    val = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        q = float("-inf")
        for j in range(i):
            q = max(q, value[j]+val[i-j-1])
        val[i] = q
        
    return val[n]
    

value = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = len(value)

print(rod_cutting_recurr(n, value))
print(rod_cutting_recurr_old(n, value))
print(rod_cutting(n, value))