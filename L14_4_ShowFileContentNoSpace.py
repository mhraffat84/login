file = open("test.txt", "r")   # open file in read mode
content=file.readlines()        # read the content of the file line by line
for line in content:           # iterate through the content
    print(line.strip())        # print the content of the file without spaces
file.close()                   # close file