
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


db.create_all()


@app.route('/00-homework')
def xhr_a():
    return render_template('00-homework.html')


@app.route('/00-server')
def server():
    # 判断数据是否存在login
    # 得到数据
    # 接收前端传递过来的数据
    name = request.args.get('lname')
    # 判断数据和数据库中login表的数据是否一致
    if Login.query.filter_by(lname=name).first():
        # 一致的话返回用户名称已存在
        return '用户名称已存在'
    else:
        return '通过'





if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')