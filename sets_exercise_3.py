'''
age = [22, 19, 24, 25, 26, 24, 25, 24]
1.Convert the ages to a set and compare the length of the list and the set, which one is bigger?
2.I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
'''

age = [22, 19, 24, 25, 26, 24, 25, 24]
s = set(age)
print(s)

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(len(unique_words))