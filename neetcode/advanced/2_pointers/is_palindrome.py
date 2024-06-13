def is_palindrome(arr: list[int]) -> bool:
    L, R = 0, len(arr) - 1

    while L < R:
        if arr[L] != arr[R]:
            return False
        L += 1
        R -= 1

    return True


print(is_palindrome([1, 2, 7, 7, 2, 1]))
