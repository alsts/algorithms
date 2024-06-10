def fib(n):
    if n < 2:
        return n

    dp = [0, 1]
    i = 2

    while i <= n:
        # perform swap
        dp[0], dp[1] = dp[1], dp[0] + dp[1]
        i += 1

    return dp[1]


def fib_nice(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


print(fib(0))
