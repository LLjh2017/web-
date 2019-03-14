from flask import Flask, render_template

app = Flask(__name__)

@app.route('/01-var/<int:num>')
def var_views(num=None):

    name = '隔壁老王'
    age = 32
    salary = 125.55
    tup = ('老魏','老王','老吕','小梦梦')
    list = ['漩涡鸣人','小智']
    dic = {
        'C':'CHINA',
        'A':'AMERICA',
        'J':'JAPAN',
    }

    dog = Dog()
    return render_template('01-var.html',params=locals())


class Dog(object):
    name = '旺财'
    def eat(self):
        return self.name + "吃狗粮"





if __name__ == "__main__":
    app.run(debug=True)