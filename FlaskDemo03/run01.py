from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/01-parent')
def parent():
    return render_template('01-parent.html')

@app.route('/02-child')
def child():
    return render_template('02-child.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.route('/03-request')
def request_views():
    # 获取请求的方案
    scheme = request.scheme
    method = request.method
    cookies = request.cookies
    args = request.args
    form = request.form
    headers = request.headers
    path = request.path
    full_path = request.full_path
    url = request.url
    return render_template('03-request.html',params=locals())

@app.route('/04-form')
def form():
    return render_template('04-form.html')

@app.route('/05-get',methods=['post','get'])
def get_views():
    uname = request.args.get('uname','')
    upwd = request.args.get('upwd', '')
    return "<h1>姓名:%s 密码:%s</h1>"%(uname,upwd)

@app.route('/06-form',methods=['POST','GET'])
def form_views():
    if request.method == 'GET':
        return render_template('06-form.html')
    else:
        print(request.form['uname'])
        return 'ok'


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')