'''
The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
1.Sort the list and find the min and max age
2.Add the min age and the max age again to the list
3.Find the median age (one middle item or two middle items divided by two)
4.Find the average age (sum of all items divided by their number )
5.Find the range of the ages (max minus min)
6.Compare the value of (min - average) and (max - average), use abs() method
'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(f"Max age - {ages[len(ages) - 1]}, Min age - {ages[0]}")

sum = 0
for age in ages:
    sum += age
avg_age = sum/ len(ages)

print(f"Avg age : {avg_age}")
print(f"Range : {ages[-1] - ages[0]}")

max = ages[-1]
min = ages[0]

print(f"{abs(min - avg_age)} == {abs(max - avg_age)}")

