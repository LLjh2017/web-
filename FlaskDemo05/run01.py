from flask import Flask, request, redirect
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()


app=Flask(__name__)

# 指定数据库的配置
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost:3306/flask"
# 指定当视图执行完毕后，自动提交数据库操作
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
# 指定每次执行操作时打印原始的SQL语句
app.config['SQLALCHEMY_ECHO']=True
# 创建数据库的实例
db = SQLAlchemy(app)


# 创建实体类
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),nullable=False,unique=True)
    age = db.Column(db.Integer)
    email = db.Column(db.String(120),unique=True)
    isActive = db.Column(db.Boolean,default=True)
    # 增加关联属性和反向引用关系
    wife = db.relationship('Wife',backref='user',uselist=False)
    def __init__(self,username,age,email):
        self.username = username
        self.age = age
        self.email = email

    def __repr__(self):
        return "<Users:%s>" % self.username

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key=True)
    sname = db.Column(db.String(30),nullable=False)
    sage = db.Column(db.Integer)

    # 增加对Classes的一(Classes)对多(Student)的引用关系
    classes_id = db.Column(db.Integer, db.ForeignKey('classes.id'))

    def __init__(self,sname,sage):
        self.sname = sname
        self.sage = sage
    def __repr__(self):
        return "<Student:%r>"%self.sname

class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer)
    tbirth = db.Column(db.Date)
    # 增加一个列(外键)  引用自course表的主键
    course_id = db.Column(db.Integer,db.ForeignKey("course.id"))

    def __init__(self,tname,tage,tbirth):
        self.tname = tname
        self.tage = tage
        self.tbirth = tbirth
    def __repr__(self):
        return "<Teacher:%r>"%self.tname

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)

    # 增加关联属性和反向引用关系
    # 关联属性 在course对象中通过哪个属性能够得到对应的所有的teacher
    # 反向引用 在teacher对象中通过哪个属性能够得到他对应的course
    teachers = db.relationship('Teacher', backref="course", lazy="dynamic")

    def __init__(self,cname):
        self.cname = cname
    def __repr__(self):
        return "<Course:%r>"%self.cname

class Classes(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30),nullable=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return "<Classes:%r>" % self.name

    # 增加关联属性和反向引用关系
    students = db.relationship('Student',backref='classes',lazy='dynamic')


class Wife(db.Model):
    __tablename__ = 'wife'
    id = db.Column(db.Integer,primary_key=True)
    wname = db.Column(db.String(30))
    # 增加对 Users 的一对一的引用关系
    users_id = db.Column(db.Integer,db.ForeignKey("users.id"))


# 将创建好的实体类映射回数据库
db.create_all()


@app.route('/01-add')
def add_views():
    # 创建Users对象,并插入到数据库中
    users = Users('王老师',35,'mrwang@163.com')
    db.session.add(users)
    # db.session.commit()
    return 'Add OK'


@app.route('/02-register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('02-register.html')
    else:
        # 接收前端传递过来的数据
        uname = request.form.get('uname')
        uage = request.form.get('uage')
        uemail = request.form.get('uemail')
        # 将数据构建成实体对象
        user = Users(uname,uage,uemail)
        # 将数据保存回数据库
        db.session.add(user)
        # db.session.commit()
        return "Register Success"

@app.route('/03-query')
def query_views():
    query = db.session.query(Users).all()
    print(query)
    return "Query OK"


@app.route('/04-queryall')
def queryall():
    users = Users.query.filter_by(isActive=True).all()
    return render_template('04-queryall.html',users=users)


@app.route('/05-update',methods=['GET','POST'])
def update_views():

    if request.method == 'GET':

        # 接收前端传递过来的参数 id
        id = request.args.get('id')
        # 根据id查询出对应的对象
        user = Users.query.filter_by(id=id).first()
        # 将查询出来的对象发送到05-update.html中进行显示
        return render_template('05-update.html',user=user)
    else:
        # 查
        id = request.form.get('id')
        user = Users.query.filter_by(id=id).first()
        # 改
        username = request.form.get('uname')
        age = request.form.get('uage')
        email = request.form.get('uemail')
        user.username = username
        user.age = age
        user.email = email
        # 保存
        db.session.add(user)
        return redirect('/04-queryall')


@app.route('/07-delete')
def delete():
    # 查
    id = request.args.get('id')
    user = Users.query.filter_by(id=id).first()
    # 删
    # db.session.delete(user)
    # 以修改来表示删除：将users表的isActive的值更改为false
    user.isActive = False
    db.session.add(user)
    return redirect('/04-queryall')


@app.route('/08-insert')
def insert_views():
    c1 = Course('钢管舞')
    c2 = Course('爵士舞')
    db.session.add(c1)
    db.session.add(c2)
    db.session.commit()
    return "Insert OK"


@app.route('/09-register-teacher')
def register_teacher():
    # 方案1 通过关联属性关联数据
    # teal = Teacher('魏老师',40,'1985-10-01')
    # teal.course_id = 1
    # db.session.add(teal)

    # 方案2 通过反向引用属性关联数据
    tea2 = Teacher('王老师',45,'1975-10-01')
    # 查询ID为1的Course的信息
    course = Course.query.filter_by(id=1).first()
    tea2.course = course
    db.session.add(tea2)

    return 'Register Teacher OK'

@app.route('/10-query')
def query10_views():
    # 通过course对象查询对应所有的teacher们
    course = Course.query.filter_by(id=1).first()
    # teachers提供了对应的teacher的查询
    teachers = course.teachers.all()
    print("课程名称:"+course.cname)
    print("对应的老师们:")
    for tea in teachers:
        print("姓名:%s,生日:%s"%(tea.tname,tea.tbirth))

    # 通过 teacher 得到对应的 course
    tea = Teacher.query.filter_by(id=1).first()
    # 得到course的对象
    course = tea.course
    print("教师姓名:%s"%tea.tname)
    print("所教课程:%s"%course.cname)
    return 'Query OK'

# 1.增加实体类Classes表示一个班级
# id:班级的id，主键自增
# name:班级名称
# 2.增加Classes对Student一对多增加关联属性以及反向引用关系
# 3.向Classes表中增加2~3条数据
#    1  1806
#    2  1807
#    3  1808
# 4.访问路径/11-register-stu
#   1.get请求的话
#   2.post请求的话，将 姓名 年龄 班级 保存进数据库
# 5.访问路径/12-students


@app.route('/11-register-stu',methods=['GET','POST'])
def register_stu():
    if request.method == 'GET':
        # 查询 classes 表中所有的数据
        list = Classes.query.all()
        return render_template('11-register-stu.html',list=list)
    else:
        # 先获取前端提交的数据
        sname = request.form.get('sname')
        sage = request.form.get('sage')
        classes_id = request.form.get('classes')
        # 构建Student对象
        stu = Student(sname,sage)
        stu.classes_id = classes_id
        # 将对象保存进数据库
        db.session.add(stu)
        return redirect('/12-students')


@app.route('/12-students')
def student():
    list = Student.query.all()
    return render_template('/12-students.html',list=list)



@app.route('/13-wife')
def wife_users():
    # 通过wife找users
    # wife = Wife.query.filter_by(id=3).first()
    # user = wife.user
    # print('Wife:%s'% wife.wname)
    # print('User:%s' % user.username)
    # 通过users找wife
    user = Users.query.filter_by(id=3).first()
    wife = user.wife
    print('Wife:%s' % wife.wname)
    print('User:%s' % user.username)
    return 'Query OK'
    

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')