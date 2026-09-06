

"""
Problem: Coin Change
Difficulty: Medium

Problem Statement:
You are given a list of coin denominations and a target amount.
You can use each coin any number of times.

Find the minimum number of coins required to make the target amount.
If it is impossible, return -1.

Input:
First line: N (number of coin types)
Second line: N space-separated coin values
Third line: Target amount

Output:
Print the minimum number of coins, or -1 if the amount cannot be formed.

Time Complexity: O(N * Amount)
Space Complexity: O(Amount)
"""

# Input
n = int(input())
coins = list(map(int, input().split()))
amount = int(input())

# dp[i] = minimum number of coins needed to make amount i
dp = [amount + 1] * (amount + 1)
dp[0] = 0

for total in range(1, amount + 1):
    for coin in coins:
        if coin <= total:
            dp[total] = min(dp[total], dp[total - coin] + 1)

# Output
if dp[amount] == amount + 1:
    print(-1)
else:
    print(dp[amount])
