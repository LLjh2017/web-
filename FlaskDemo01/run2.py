from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/<int:num>')
@app.route('/index/<int:num>')

def index(num=None):
    if not num:
        num = 1
    return "您访问的是第%d页" % num


@app.route('/admin/login/form/show')
def show():
    return "路径"

@app.route('/url')
def url():
    url = url_for('show')
    return "<a href='%s'>去往show</a>" % url

if __name__ == "__main__":
    app.run(debug=True)