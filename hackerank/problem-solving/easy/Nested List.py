"""
Platform: HackeRank
Problem: Nested Loops for second lowest grade
Difficulty: easy
Concepts: Nested loops, list comprehension, loops
"""

N = int(input())
records = []
scores = []
final = []

for i in range(N):
    x = input()
    y = float(input())
    scores.append(y)
    z = [x,y]
    records.append(z)
j = min(scores)
j = min(scores)
scores = [i for i in scores if i != j]
for i in records:
    if i[1] == min(scores):
        final.append(i[0])
    else: 
        pass
final.sort()
for i in final:
    print(i)
