from flask import Flask # Import the Flask class from the flask module
app = Flask(__name__) # Create an instance of the Flask class called app
@app.route('/') # Define the route for the default URL

def home(): # Define the home() function
    return "Hello, this is back-end server!" # Return the string

if __name__ == '__main__': # If the script is executed
    app.run(debug=True) # Run the app in debug mode