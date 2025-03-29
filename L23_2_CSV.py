import csv 

# write data to a CSV file
with open("data.csv", "w", newline="") as file: # open fil in writer mode
    writer = csv.writer(file) # create a writer object
    writer.writerow(["name" , "age" , "email"]) # write header of a table as a csv file
    writer.writerow(["Ahmed", 25, "ahmed@emeil.acom"]) # write data to the file

# read data from CSV file
with open("data.csv", "r") as file: # open file in read mode
    reader = csv.reader(file) # create a reader object
    for row in reader: # iterate over rows
        print(row)  # print each row in terminal