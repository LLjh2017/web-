from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()




app =Flask(__name__)

# 为app指定数据库的配置信息
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/flask'
# 创建SQLAlchemy的数据库实例
db=SQLAlchemy(app)

# 创建模型类 - Users,映射到数据库叫users表
# 创建字段 id ,主键,自增
# 创建字段 username 长度为80的字符串 不允许为空 值要唯一
# 创建字段 age 整数
# 创建字段 email 长度为120的字符串 必须唯一

class Users(db.Model)
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),nullable=False,unique=True)




@app.route('/')
def index():
    print(db)
    return '创建db成功'

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')