import time

def fib_recurr(n):
    if n == 0 or n == 1:
        return 1
    return fib_recurr(n-1) + fib_recurr(n-2)

def fib(n):
    ans = [0] * (n+1)
    ans[0] = 1
    ans[1] = 1

    for i in range(2, n+1):
        ans[i] = ans[i-1] + ans[i-2]
    return ans[n]


start_time = time.time()
print(fib_recurr(20))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(fib(20))
print("--- %s seconds ---" % (time.time() - start_time))