from flask import Flask,jsonify  # Import Flask to create a web server and jsonify to return JSON data

app = Flask(__name__)  # Create a Flask web server instance called app

@app.route('/api/greeting', methods=['GET'])  # Define the route for the API

def greeting():  # Define the function that will be called when the route is accessed
    return jsonify({'message': "Hello, WElcome to our API!"})  # Return a JSON response

if __name__ == "__main__": # Check if the code is executed as the main program
    app.run(debug=True)  # Start the Flask web server with the debug mode enabled