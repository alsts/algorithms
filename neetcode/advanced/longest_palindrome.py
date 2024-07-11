# Time: O(n^2), Space: O(n)
def longest_palindrome(s):
    length = 0
    for char_id in range(len(s)):
        # odd length
        length = max(length, helper(s, char_id, char_id))

        # even length
        length = max(length, helper(s, char_id, char_id + 1))
    return length


def helper(s, l, r):
    max_length = 0
    # if not out of bounds and characters match -> expand outwards
    while l >= 0 and r < len(s) and s[l] == s[r]:
        new_length = r - l + 1
        if new_length > max_length:
            max_length = new_length

        l -= 1
        r += 1
    return max_length


print(longest_palindrome('abaab'))
