from typing import List

def knapsack_recurr(value: List[int], weight: List[int], W: int):
    n = len(value)

    if n == 0 or W == 0:
        return 0
    
    if weight[n-1] > W:
        return knapsack_recurr(value[:n-1], weight[:n-1], W)
    
    return max(knapsack_recurr(value[:n-1], weight[:n-1], W), knapsack_recurr(value[:n-1], weight[:n-1], W-weight[n-1])+value[n-1])


def knapsack(value: List[int], weight: List[int], W: int):
    n = len(value)
    c = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            if w < weight[i-1]:
                c[i][w] = c[i-1][w]
            else:
                c[i][w] = max(c[i-1][w], c[i-1][w-weight[i-1]]+value[i-1])

    for i in range(n+1):
        print(c[i])
    return c[n][W]

value = [5, 10, 2, 4, 8]
weight = [3, 4, 2, 1, 5]
W = 10

print(knapsack_recurr(value, weight, W))
print(knapsack(value, weight, W))
