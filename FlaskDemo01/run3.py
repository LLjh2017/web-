from flask import Flask, render_template

app = Flask(__name__)


@app.route('/01-temp')
def temp():
    str = render_template('01-temp.html')
    return str


if __name__ == "__main__":
    app.run(debug=True)