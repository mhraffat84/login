import array

# Create an array of integers
numbers = array.array('i', [10, 20, 30, 40, 50])

searchValue = int(input("Enter a value to search for: "))
# we used int() to convert the input to an integer
# because the input function returns a string
if searchValue in numbers:
    print("Yes,", searchValue, "is in the array")
else:
    print("No,", searchValue, "is not in the array")