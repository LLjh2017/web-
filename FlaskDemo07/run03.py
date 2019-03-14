from flask import Flask, request, session, render_template,redirect,make_response
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app=Flask(__name__)
# 配置session
app.config['SECRET_KEY']='aixieshaxiesha'
# 连接数据库
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/flask"
# 视图完成自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)


class Users_Vip(db.Model):
    __tablename__='users_vip'
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(80), nullable=False, unique=True)
    lpwd = db.Column(db.Integer)
    uname = db.Column(db.String(80))
    isActive = db.Column(db.Boolean, default=True)

db.create_all()

@app.route('/06-login',methods=['GET','POST'])
def login06():
    if request.method == 'GET':
        # 判断session中是否有登录信息
        if 'id' in session and 'lname' in session:
            # 已经成功登陆过
            return redirect('/')
        else:
            # 没有成功登陆过
            # 判断cookies中是否有登录信息
            if 'id' in request.cookies and 'lname' in request.cookies:
                # cookies中有登录信息
                # 从cookies中取出数据保存到session
                id = request.cookies['id']
                lname = request.cookies['lname']
                session['id'] = id
                session['lname'] = lname
                return redirect('/')
            else:
                # cookies中没有登录信息
                return render_template('/06-login.html')
    else:
        # 处理post请求
        # 接收前端传递过来的数据并验证登录是否成功
        uname = request.form.get('uname')
        upwd = request.form.get('upwd')
        login = Users_Vip.query.filter(Users_Vip.lname==uname,
                               Users_Vip.lpwd==upwd).first()
        print(type(login))
        if login:
            # 登录成功
            # 将信息保存进session
            session['lname'] = uname
            session['id'] = login.id

            # 创建响应对象
            resp = redirect('/')

            # 判断是否将数据保存进cookie
            if 'isSaved' in request.form:
                mAge = 60*60*24*365
                resp.set_cookie('id',str(login.id),mAge)
                resp.set_cookie('lname', uname,mAge)
            return resp
        else:
            # 登录失败
            errMsg='用户名或密码不正确'
            return render_template('06-login.html',errMsg=errMsg)

@app.route('/')
def index():
    # 登录信息的处理
    # 判断session是否有登录信息
    if 'id' in session and 'lname' in session:
        lname = session.get('lname')
        return render_template('index.html',lname=lname)
    else:
        if 'id' in request.cookies and 'lname' in request.cookies:
            # cookies中有登录信息
            id = request.cookies.get('id')
            lname = request.cookies.get('lname')
            session['id'] = id
            session['lname'] = lname
            return render_template('index.html',lname=lname)
        else:
            # cookies中没有登录信息
            return render_template('index.html')


@app.route('/logout')
def logout():
    resp = redirect('/')
    if 'id' in session and 'lname' in session:
        del session['id']
        del session['lname']
    if 'id' in request.cookies and 'lname' in request.cookies:
        resp.delete_cookie('id')
        resp.delete_cookie('lname')
    return resp


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')