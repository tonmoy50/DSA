# Python3 implementation of the approach


# Function to return the minimum
# number of delete operations
def findMinimumDeletion(l, r, dp, s):
    if l > r:
        return 0
    if l == r:
        return 1
    if dp[l][r] != -1:
        return dp[l][r]

    # When a single character is deleted
    res = 1 + findMinimumDeletion(l + 1, r, dp, s)

    # When a group of consecutive characters
    # are deleted if any of them matches
    for i in range(l + 1, r + 1):
        # When both the characters are same then
        # delete the letters in between them
        if s[l] == s[i]:
            res = min(
                res,
                findMinimumDeletion(l + 1, i - 1, dp, s)
                + findMinimumDeletion(i, r, dp, s),
            )

    # Memoize
    dp[l][r] = res
    return res


# Driver code
if __name__ == "__main__":
    s = "xyyzqqqzzq"
    n = len(s)
    N = 10
    dp = [[-1 for i in range(N)] for j in range(N)]
    print(findMinimumDeletion(0, n - 1, dp, s))
