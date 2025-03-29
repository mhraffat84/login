import random # import random module
import string # import string module (Letters - digits - punctuation - whitespace)

def password_generator(length): # define function to create password with number of characters defined by user
    characters = string.ascii_letters + string.digits + string.punctuation  # define characters to be used in password
    password = ''.join(random.choice(characters) for _ in range(length)) # create password with random characters from the defined characters
    return password # save password in function

# Run Program
password_Length = int(input("Enter the length of the password: ")) # ask user to enter the length of the password
password = password_generator(password_Length) # call function to create password with the length defined by user
print("")
print(f"Your Generated Password is: {password}") # print the generated password to user
print("")