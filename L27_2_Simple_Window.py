import tkinter as tk

# Create window
window = tk.Tk()
window.title("A Simple Interface")
window.geometry("500x300")

# Add a label
label = tk.Label(window, text="Insert Your Name: ", font=("Arial", 14)) #to show a text with specific options
label.pack(pady=10) # to show the label

# Add Textbox = Entry
entry = tk.Entry(window, font=("Arial",14))
entry.pack(pady=10)

# Create a Function
def greet():
    name = entry.get() # to get user inputs
    greet_label.config(text=f"Welcome, {name}!")


# Add a button
button = tk.Button(window, text="Click Here", font=("Arial", 14), command=greet)
button.pack(pady=10)

# Add text label
greet_label = tk.Label(window, text="", font=("Arial", 14))
greet_label.pack(pady=10)


# Run Window
window.mainloop()