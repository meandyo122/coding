from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/next')
def next_page():
    return "<h1>Welcome to the next page!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
