try:
    file=open("test.txt","r")   # open file in read mode
    content = file.read()       # read the content of the file
    print(content)              # print the content of the file
    file.close()                # close file
except FileNotFoundError:
    print("File not found")