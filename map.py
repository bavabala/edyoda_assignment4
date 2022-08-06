# 2) Write a Python program to triple all numbers of a given list of integers. Use Python map.

#list of given numbers:
sample_list= [1,2,3,4,5,6,7]
print("original_list", sample_list)

#using map function
result = map(lambda value: value + value + value, sample_list) 
print("\nTriple of list numbers")

#print the list
print(list(result))