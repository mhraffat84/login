import sqlite3 # Import the sqlite3 module

# Connect to the database
conn = sqlite3.connect('tasks.db')  # اسم قاعدة البيانات - سيتم إنشاءها في نفس مجلد المشروع
#conn = sqlite3.connect('c:/myfolder/tasks.db')  # اسم قاعدة البيانات - سيتم إنشاءها في المجلد المحدد
cursor = conn.cursor()  # Create a cursor object

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL)
""")  # Create a table named tasks with two columns: id and name

conn.commit()  # Save (commit) the changes
conn.close()  # Close the connection
print("The table has been created successfully")  # Print a message

# Add a record
conn = sqlite3.connect('tasks.db') # Connect to the database
cursor = conn.cursor()  # Create a cursor object
task_name = "Learrn SQLite in Python"
cursor.execute("INSERT INTO tasks(name) VALUES(?)", (task_name,)) # Add a new record to the table"
conn.commit()  # Save (commit) the changes
conn.close()  # Close the connection
print("The record has been added successfully")  # Print a message

# Show all records
conn = sqlite3.connect('tasks.db') # Connect to the database
cursor = conn.cursor()  # Create a cursor object
cursor.execute("SELECT * FROM tasks")  # Select all records from the table called tasks
tasks = cursor.fetchall()  # Fetch all records
conn.close()  # Close the connection
for task in tasks:  # Loop through the records
    print(f"ID: {task[0]}, Task: {task[1]}")  # Print the record