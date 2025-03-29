from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['UserName']
    return f"Welcome, {username}!"

if __name__ == '__main__':
    app.run(debug=True)
