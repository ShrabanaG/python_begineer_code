'''
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
Exercises: Level 2
1.Join A and B
2.Find A intersection B
3.Is A subset of B
4.Are A and B disjoint sets
5.Join A with B and B with A
6.What is the symmetric difference between A and B
7.Delete the sets completely
'''

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(f'\nJoin A and B: {A.union(B)}')
print(f'\nintersection A and B: {A.intersection(B)}')
print(f'\n Is A subset of B? {A.issubset(B)}')
print(f"\n symmetric {A.symmetric_difference(B)}")