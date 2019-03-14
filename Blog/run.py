from flask import Flask, render_template, request, redirect, make_response

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        # 去看login.html模板
        return render_template('login.html')
    else:
        # 接收前端请求提交的数据
        username=request.form['username']
        password=request.form['password']
        # 如果用户名是admin并且密码也是admin,去/路径
        if username=='admin' and password=='admin':
            # 登陆成功,重定向去'/'
        # return "用户名：%s,密码：%s" % (username,password)
            return redirect('/')
        else:
            # 使用响应对象输出"用户名或密码不正确"
            resp = make_response("用户名或密码不正确")
            return resp

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        username=request.form['username']
        email=request.form['email']
        url=request.form['url']
        password = request.form['password']
        return "用户名：%s,邮箱：%s,网页：%s,密码：%s" % (username,email,url,password)



if __name__=="__main__":
    app.run(debug=True)
