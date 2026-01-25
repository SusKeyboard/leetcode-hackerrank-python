"""
Platform: HackerRank 
Problem: Coordinates from given x y z with constraint of sum
Difficulty: easy
Concepts: List comprehension
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [
    [i,j,k]
    for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1)
    if i + j + k != n
]

print(result)
