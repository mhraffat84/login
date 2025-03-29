import json 

# data to be written to a JSON file
user_data={"name" : "Ahmed" , "age" : 25 , "email" : "ahmed@email.com"}

# create json file
with open("data.json", "w") as file: # open file in write mode
    json.dump(user_data, file) # write data to file
    print("Data written successfully")

# read data from json file
with open("data.json", "r") as file: # open file in read mode
    data = json.load(file) # read data from file
    print(data) # print data in terminal