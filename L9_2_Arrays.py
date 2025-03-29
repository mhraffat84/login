import array

# Create an array of integers
numbers = array.array('i', [10, 20, 30, 40, 50])

# Print the array
print(numbers)

# add 60 to the array
numbers.append(60)
print(numbers)

# remove 30 from the array
#numbers.remove(30)
#print(numbers)

# count the array items
print(len(numbers))

# check if the array contains 30
if 30 in numbers:
    print("Yes, 30 is in the array")
else:
    print("No, 30 is not in the array")