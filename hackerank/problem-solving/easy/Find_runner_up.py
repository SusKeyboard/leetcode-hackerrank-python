"""
Platform: HackerRank 
Problem: Find runner up score
Difficulty: easy
Concepts: array and list comprehension
"""
n = int(input())
A = list(map(int, input().split() ))

max_score = max(A)
arr =[ x for x in A if x != max_score]

result = max(arr)

print(result)
