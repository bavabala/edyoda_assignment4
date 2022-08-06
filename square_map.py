# 3)Write a Python program to square the elements of a list using map() function.

#function
def square_number(nums):
    return nums * nums
#given number
nums = [4,5,2,9]
print("Sample_list: ",nums)

#using map function
value = map(square_number,nums)
print("Square element of the list:")

#print the square of the list
print(list(value))
