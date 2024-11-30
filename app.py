from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/next')
def next_page():
    return "<h1> Welcome to the next page! <h1>"

if __name__ == '__main__':
    app.run(debug=True)
