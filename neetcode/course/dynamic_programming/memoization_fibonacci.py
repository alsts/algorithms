
# Memoization - Top to Bottom Dynamic Programming
def fib(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    return cache[n]


print(fib(5, {}))
