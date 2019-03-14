import json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()



app=Flask(__name__)

# 指定数据库的配置
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/flask"

# 指定当视图执行完毕后，自动提交数据库操作
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True


# 创建数据库实例
db=SQLAlchemy(app)

# 创建实体类
class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer,primary_key=True)
    lname = db.Column(db.String(30),nullable=False,unique=True)
    lpwd = db.Column(db.String(30))
    uname = db.Column(db.String(30))

    def to_dict(self):
        dic={
            'id':self.id,
            'lname':self.lname,
            'lpwd':self.lpwd,
            'uname':self.uname
        }
        return dic


db.create_all()

@app.route('/00-homework')
def homework():
    return render_template('00-homework.html')


@app.route('/00-server')
def server00():
    # 判断数据是否存在login
    # 得到数据
    # 接收前端传递过来的数据

    # 判断数据和数据库中login表的数据是否一致
    # 一致的话返回用户名称已存在

    lname=request.args.get('lname')
    login=Login.query.filter_by(lname = lname).first()
    if login:
        return '用户名称已存在'
    else:
        return '通过'


@app.route('/01-post')
def post():
    return render_template("01-post.html")


@app.route('/01-server',methods=['POST'])
def server01():
    uname = request.form['uname']
    uage = request.form['uage']
    return "传递过来的uname的值为:%s,传递过来的uage的值为：%s"%(uname,uage)

@app.route('/02-form',methods=['GET','POST'])
def form():
    if request.method=='GET':
        return render_template('02-form.html')
    else:
        uname = request.form['uname']
        uage = request.form['uage']
        return "传递过来的uname的值为:%s,传递过来的uage的值为：%s" % (uname, uage)


@app.route('/03-getlogin')
def getlogin():
    return render_template('03-getlogin.html')

@app.route('/03-server')
def server03():
    logins = Login.query.all()
    strl = ""
    for login in logins:
        strl += str(login.id)
        strl += login.lname
        strl += login.lpwd
        strl += login.uname

    return strl

@app.route('/04-json')
def json_views():
    return render_template("04-json.html")


@app.route('/04-server')
def server04():
    # list=["王老师","RapWang","隔壁老王"]
    # 将list转换为json格式的字符串
    # dic={
    #     "name":"wanglaoshi",
    #     "age":35,
    #     "gender":"male"
    # }
    list=[
        {
            'name':'wang',
            'age':30,
            'gender':'male'
        },
        {
            'name': 'li',
            'age': 90,
            'gender': 'female'
        }
    ]
    jsonStr = json.dumps(list)
    return jsonStr

@app.route('/05-json-login')
def json_login():
    return render_template('05-json-login.html')

@app.route('/05-server')
def server05():
    # 得到id为1的Login的信息
    login = Login.query.filter_by(id=1).first()
    # dic = {
    #     'id': login.id,
    #     'lname': login.lname,
    #     'lpwd': login.lpwd,
    #     'uname': login.uname
    # }
    jsonStr = json.dumps(login.to_dict())
    return jsonStr




if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')