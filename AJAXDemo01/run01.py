
from flask import Flask, render_template, request

app=Flask(__name__)




@app.route('/01-xhr')
def xhr():
    return render_template('01-xhr.html')

@app.route('/server')
def server():
    uname = request.args.get('uname')

    return "<h1>%s</h1>"%uname

@app.route('/02-server')
def xhr_a():
    return render_template('02-server.html')


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')