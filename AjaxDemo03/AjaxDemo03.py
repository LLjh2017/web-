import json

from flask import Flask, request
import pymysql
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/flask"
db = SQLAlchemy(app)

class Login(db.Model):
    __tablename__ = "login"
    id = db.Column(db.Integer,primary_key=True)
    lname = db.Column(db.String(30))
    lpwd = db.Column(db.String(30))
    uname = db.Column(db.String(30))

    def to_dict(self):
        dic = {
            'id':self.id,
            'lname' : self.lname,
            'lpwd' : self.lpwd,
            'uname' : self.uname,
        }
        return dic

class Province(db.Model):
    __tablename__ = 'province'
    id=db.Column(db.Integer,primary_key=True)
    pname=db.Column(db.String(30))
    cities = db.relationship("City",backref="province",lazy="dynamic")
    def to_dict(self):
        dic = {
            "id":self.id,
            "pname":self.pname,
        }
        return dic

class City(db.Model):
    __tablename__ = "city"
    id=db.Column(db.Integer,primary_key=True)
    cname=db.Column(db.String(30))
    pid=db.Column(db.Integer,db.ForeignKey('province.id'))

    def to_dict(self):
        dic = {
            'id':self.id,
            'cname':self.cname,
            'pid':self.pid,
        }
        return dic

db.create_all()

@app.route('/00-server')
def server00():
    # 查询 Login 中的所有的数据
    logins = Login.query.all()
    # 再将所有的数据转换成JSON格式的字符串
    list = []
    for l in logins:
        list.append(l.to_dict());
    return json.dumps(list)

@app.route('/01-loadprovince')
def loadprovince():
    provinces = Province.query.all()
    list = []
    for pro in provinces:
        list.append(pro.to_dict())
    return json.dumps(list)

@app.route('/01-loadcity')
def loadcity():
    pid = request.args.get('pid')
    cities = City.query.filter_by(pid=pid).all()
    list = []
    for city in cities:
        list.append(city.to_dict())
    return json.dumps(list)

@app.route('/02-jq-load',methods=['POST'])
def jq_load():
    # 获取使用get方式提交的数据
    # uname=request.args.get('uname')
    # uage =request.args.get('uage')
    # return "使用get方式传递进来的数据为:uname=%s,uage=%s" % (uname,uage)

    # 获取使用post方式提交的数据
    uname=request.form.get('uname')
    uage=request.form.get('uage')
    return "使用Post方式提交过来的数据:uname=%s,uage=%s" % (uname,uage)

    # return "这是使用Load方法完成的异步响应"

@app.route('/03-jq-get')
def jq_get():
    dic = {
        "uname" : "王老师",
        "uage" : 30,
    }
    return json.dumps(dic)

@app.route('/04-jq-post',methods=['POST'])
def jq_post():
    uname=request.form.get('uname')
    ugender = request.form.get('ugender')
    return "提交的数据为:uname=%s,ugender=%s" % (uname,ugender)

@app.route('/05-login')
def login_views():
    lname = request.args.get('lname')
    login=Login.query.filter_by(lname=lname).first()
    if login:
        dic = {
            'status' : 1,
            'text' : '用户名称已经存在'
        }
    else:
        dic = {
            'status' : 0,
            'text' : '通过'
        }
    return json.dumps(dic)


@app.route('/05-server',methods=['POST'])
def server05():
    lname = request.form.get('lname')
    lpwd = request.form.get('lpwd')
    uname = request.form.get('uname')
    login = Login()
    login.lname = lname
    login.lpwd = lpwd
    login.uname = uname
    try:
        db.session.add(login)
        db.session.commit()
        dic = {
            'status':1,
            'text' : '注册成功'
        }
    except Exception as e:
        print(e)
        dic = {
            'status':0,
            'text' : '注册失败'
        }

    return json.dumps(dic)

@app.route("/06-jq-ajax")
def jq_ajax():
    logins = Login.query.all()
    list = []
    for l in logins:
        list.append(l.to_dict())
    return json.dumps(list)

if __name__ == '__main__':
    app.run(debug=True)













