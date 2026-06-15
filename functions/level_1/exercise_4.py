# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(list):
    result = []
    for i in range(len(list) - 1, -1, -1):
        result.append(list[i])
    return result    

print(reverse_list([1,2,3,4,5,67,8,9,10]))