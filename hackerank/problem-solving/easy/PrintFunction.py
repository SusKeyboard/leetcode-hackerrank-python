"""
Platform: HackerRank
Problem: Print a string of numbers
Difficulty: easy
Concepts: Loops and strings
"""

n = int(input())
k =""
if 1 <= n <= 150:
    for i in range(1,n+1):
        k += str(i)
print(k)
