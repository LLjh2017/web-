import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/01-server')
def server01():
    # 接收前端传递过来的参数 - callback
    cb = request.args.get('callback')
    print(cb)
    print(type(cb))

    return cb+"('这是服务器端响应的内容');"

@app.route('/02-server')
def server02():
    cb = request.args.get('callback')
    dic = {
        'flightNO' : 'CA977',
        'from' : 'Beijing',
        'to' : 'LA',
        'time' : '00:30',
    }
    jsonStr = json.dumps(dic)
    return cb+"("+jsonStr+");"

@app.route('/03-jq-cross')
def jq_cross():
    cb = request.args.get('callback')
    return cb+"('服务器端响应回去的数据')"

@app.route('/03-server')
def server03():
    cb = request.args.get('huidiao')
    print(cb)
    return cb+"('这是使用方案2响应的数据');"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')