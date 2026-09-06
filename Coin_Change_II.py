"""
Problem: Coin Change II
Difficulty: Medium

Problem Statement:
You are given a list of coin denominations and a target amount.
You can use each coin any number of times.

Find the total number of different combinations that can form
the target amount. The order of coins does not matter.

Input:
First line: N (number of coin types)
Second line: N space-separated coin values
Third line: Target amount

Output:
Print the number of different combinations.

Time Complexity: O(N * Amount)
Space Complexity: O(Amount)
"""

# Input
n = int(input())
coins = list(map(int, input().split()))
amount = int(input())

# dp[i] = number of ways to make amount i
dp = [0] * (amount + 1)
dp[0] = 1

# Process coins one by one to avoid counting different orders
for coin in coins:
    for total in range(coin, amount + 1):
        dp[total] += dp[total - coin]

print(dp[amount])
