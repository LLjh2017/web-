from flask import Flask, make_response, request, render_template, session

app=Flask(__name__)
app.config['SECRET_KEY']='aixieshaxiesha'


@app.route('/01-setCookie')
def setCookie():
    resp = make_response('保存cookie成功')
    # 保存 uname 进 cookie 值为 wangwc
    resp.set_cookie('uname','wangwc',3600)
    return resp


@app.route('/02-getCookie')
def getCookie():
    print(request.cookies)
    uname = request.cookies.get('uname')
    return 'uname的值为：%s'%uname

@app.route('/03-login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        # 判断 cookies中是否有 uname 的值
        if 'uname' in request.cookies:
            # 有 uname 的话 则视为保存过密码(曾经成功登陆过)
            uname = request.cookies.get('uname')
            return '欢迎：' + uname
        else:
            # 没有 uname 的话 去往 03-06-login.html 模板上
            return render_template('03-login.html')
    else:
        # 获取用户名称和密码 并判断是否登录成功
        uname = request.form.get('uname')
        upwd = request.form.get('upwd')
        if uname == 'admin' and upwd == 'admin':
            resp = make_response('欢迎：'+uname)
            # 判断是否记住密码
            if 'isSaved' in request.form:
                resp.set_cookie('uname',uname, 60 * 60 * 24 * 365)
            return resp
        else:
            return '登录失败'

@app.route('/04-setSession')
def setsession():
    session['uname'] = 'Tarena'
    return "保存session成功"

@app.route('/05-getSession')
def getSession():
    if 'uanme' in session:
        uname = session['uname']
        return 'uname:'+uname
    else:
        return "session中没有相应数据"


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")